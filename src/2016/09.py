import re
import pathlib
from functools import cache

from utils import *

data = pathlib.Path("../../data/2016/09.txt").read_text(encoding="utf-8")
compressed = data.strip()


def partition(compressed):
    while len(compressed):
        if match := re.match(r"^\((\d+)x(\d+)\)", compressed):
            yield (
                int(match.group(1)),
                int(match.group(2)),
                compressed[len(match.group(0)) :][: int(match.group(1))],
            )

            compressed = compressed[len(match.group(0)) + int(match.group(1)) :]

        elif match := re.match(r"^([A-Z ]+)", compressed):
            yield (match.group(1),)

            compressed = compressed[len(match.group(1)) :]


part_1 = 0

for chunk in partition(compressed):
    match chunk:
        case [int(size), int(repeat), str(text)]:
            part_1 += size * repeat
        case [str(text)]:
            part_1 += len(text)

print(part_1)


@cache
def decompress(compressed):
    decompressed_size = 0

    for chunk in partition(compressed):
        print(chunk)
        match chunk:
            case [int(size), int(repeat), str(text)]:
                decompressed_size += repeat * decompress(text)

            case [str(text)]:
                decompressed_size += len(text)

            case other:
                raise ValueError(other)

    return decompressed_size


compressed = re.sub(r"[A-Z]", " ", data.strip())

part_2 = decompress(compressed)

print(part_2)
