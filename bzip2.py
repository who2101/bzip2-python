import os, bz2

exts = [".bsp", ".mp3", ".wav", ".vmt", ".vtf", ".nav"]

class BZ2:
    def compress_file(path: str) -> bool:
        for ext in exts:
            if ext not in path:
                continue
            else:
                with open(path, 'rb') as file:
                    with bz2.BZ2File(path + '.bz2', 'wb') as bzipped:
                        bzipped.write(file.read())
                        return True

        return False

    def compress_folder(folder: str) -> None:
        for root, dirs, files in os.walk(folder):
            for file in files:
                if not BZ2.compress_file(os.path.join(root, file)):
                    continue
