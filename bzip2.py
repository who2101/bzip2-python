import os, bz2
from pathlib import Path

exts = [".bsp", ".mp3", ".wav", ".vmt", ".vtf", ".nav", ".mdl", ".phy", ".vvd", ".vtx", ".txt", ".ani"]

class BZ2:
    def compress_file(path: str) -> bool:
        for ext in exts:
            if Path(path).suffix == ext:
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
