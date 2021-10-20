from zlib import compress, decompress
from base64 import b64encode, b64decode
from pathlib import Path
import pickle
import os
import bson

REPO = "haapi"


def find_files(path):
    for file in path.iterdir():
        if file.is_file():
            yield file
        elif file.is_dir():
            yield from find_files(file)

def save_repo(repo, path=None):
    data = {}
    path, name = os.path.split(repo)

    for file in find_files(Path(REPO)):
        with open(file, 'rb') as f:
            data[str(file)] = compress(f.read())
    if path is None:
        path = f"{name}.repo"
    with open(path, 'wb') as f:
        pickle.dump(data, f)


