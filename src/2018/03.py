import pathlib
from collections import defaultdict

from utils import *

data = pathlib.Path("../../data/2018/03.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

lines = [ints(line) for line in lines]

fabric = defaultdict(int)
non_overlapped = set()
touched = defaultdict(set)

for claim_id, col, row, width, height in lines:
    non_overlapped.add(claim_id)

    overlapped = set()

    for w in range(width):
        for h in range(height):
            r, c = row + h, col + w

            fabric[r, c] += 1
            touched[r, c].add(claim_id)

            if len(touched[r, c]) > 1:
                overlapped.update(touched[r, c])

    if overlapped:
        for o in overlapped:
            non_overlapped.discard(o)


part_1 = len(list(filter(lambda c: c > 1, fabric.values())))

print(part_1)

part_2 = non_overlapped.pop()

print(part_2)
