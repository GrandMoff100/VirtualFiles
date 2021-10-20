import os
import pickle
import zlib

from typing import Union, Iterator
from pathlib import Path


def load_bin_content(directory: Union[str, Path]) -> bytes:
    data = {}
    _, name = os.path.split(directory)

    for file in find_files(Path(directory)):
        with open(file, 'rb') as f:
            data[str(file)] = zlib.compress(f.read())

    return pickle.dump(data, f)

def export_dir_to_bin(directory: Union[str, Path], target: Union[str, Path, None] = None) -> None:
    if target is None:
        target = "directory.data"

    with open(target, "wb") as f:
        content = load_bin_content(directory)
        f.write(content)


def find_files(path: Path) -> Iterator[Path]:
    for file in path.iterdir():
        if file.is_file():
            yield file
        elif file.is_dir():
            yield from find_files(file)
