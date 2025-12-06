import pathlib
from operator import itemgetter

from utils import *

data = (
    pathlib.Path("../../data/2025/05.txt")
    .read_text(encoding="utf-8")
    .strip()
    .split("\n\n")
)

ranges = matrix(data[0], try_parse=True, separator="-")

ids = [int(line) for line in data[1].split("\n")]

part_1 = 0

for id in ids:
    for r in ranges:
        if r[0] <= id <= r[1]:
            part_1 += 1
            break

print(part_1)

ordered_ranges = list(sorted(ranges, key=itemgetter(0)))

merged = [ordered_ranges.pop(0)]

for r in ordered_ranges:
    if r[0] - 1 <= merged[-1][1]:
        merged[-1][1] = max(merged[-1][1], r[1])
    else:
        merged.append(r)

part_2 = 0

for r in merged:
    diff = r[1] - r[0] + 1
    part_2 += diff

print(part_2)
