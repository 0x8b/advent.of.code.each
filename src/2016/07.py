import pathlib
import re

from utils import *

data = pathlib.Path("../../data/2016/07.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")


part_1 = 0
part_2 = 0

for line in lines:
    parts = line.replace("[", " ").replace("]", " ").split(" ")

    outside = " ".join(parts[::2])
    inside = " ".join(parts[1::2])

    tuples_outside = [
        t for t in zip(outside, outside[1:], outside[2:], outside[3:]) if " " not in t
    ]

    tuples_inside = [
        t for t in zip(inside, inside[1:], inside[2:], inside[3:]) if " " not in t
    ]

    if any(
        t[0] == t[3] and t[1] == t[2] and t[0] != t[1] for t in tuples_outside
    ) and all(t[0] != t[3] or t[1] != t[2] for t in tuples_inside):
        part_1 += 1

    tuples_outside = set(
        [
            t
            for t in zip(outside, outside[1:], outside[2:])
            if " " not in t and t[0] == t[2] and t[0] != t[1]
        ]
    )

    tuples_inside = set(
        [
            (t[1], t[0], t[1])
            for t in zip(inside, inside[1:], inside[2:])
            if " " not in t and t[0] == t[2] and t[0] != t[1]
        ]
    )

    if tuples_outside & tuples_inside:
        part_2 += 1

print(part_1)
print(part_2)
