import math
import pathlib

from utils import *

data = pathlib.Path("../../data/2025/09.txt").read_text(encoding="utf-8")

points = [tuple(row) for row in matrix(data, separator=",", try_parse=True)]

part_1 = 0

for a in points:
    for b in points:
        if a == b:
            continue

        area = (abs(a[0] -  b[0]) + 1) * (abs(a[1] - b[1]) + 1)

        part_1 = max(part_1, area) 

print(part_1)     