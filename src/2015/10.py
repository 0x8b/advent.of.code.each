import pathlib
from functools import cache
from itertools import groupby

data = pathlib.Path("../../data/2015/10.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

sequence = lines[0]

for i, _ in enumerate(range(50), 1):
    sequence = "".join(f"{len(list(g))}{k}" for k, g in groupby(sequence))

    if i == 40:
        print(len(sequence))

    if i == 50:
        print(len(sequence))
