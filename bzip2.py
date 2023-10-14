import bz2
import os

exts = [".bsp", ".mp3", ".wav", ".vmt", ".vtf", ".nav"]

def compress_file(path: str) -> None:
    """
    Сжимает файл в bz2 формате по указанному пути
    """

    with open(path, 'rb') as file:
        with bz2.BZ2File(path + '.bz2', 'wb') as bzipped:
            bzipped.write(file.read())

def convert(path: str) -> None:
    """
    Сжимает все файлы в bz2 по пути папки
    """

    for root, dirs, files in os.walk(path):
        for file in files:
            for ext in exts:
                if not file.endswith(ext):
                    continue
                else:
                    filepath = os.path.join(root, file)
                    compress_file(filepath)
                    print(filepath + " is compressed")