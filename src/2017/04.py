import pathlib
from collections import Counter

from utils import *

data = pathlib.Path("../../data/2017/04.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

print(lines)

part_1 = 0
part_2 = 0

for line in lines:
    if len(set(line.split(" "))) == len(line.split(" ")):
        part_1 += 1

    freqs = [
        "".join([f"{ch}{c}" for ch, c in sorted(Counter(word).items())])
        for word in line.split(" ")
    ]

    if len(set(freqs)) == len(freqs):
        part_2 += 1

print(part_1)
print(part_2)
