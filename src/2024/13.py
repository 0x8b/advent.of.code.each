import math
import pathlib
from functools import cache

from utils import *

data = pathlib.Path("../../data/2024/13.txt").read_text(encoding="utf-8")

machines = [
    [ints(line) for line in machine.strip().split("\n")]
    for machine in data.strip().split("\n\n")
]

tokens_for_a = 3
tokens_for_b = 1


@cache
def find_cheapest_way(ax, ay, an, bx, by, bn, px, py):
    if px < 0 or py < 0:
        return math.inf

    if px == 0 and py == 0:
        return an * tokens_for_a + bn * tokens_for_b

    return min(
        find_cheapest_way(ax, ay, an + 1, bx, by, bn, px - ax, py - ay),
        find_cheapest_way(ax, ay, an, bx, by, bn + 1, px - bx, py - by),
    )


part_1 = 0

for i, [[ax, ay], [bx, by], [px, py]] in enumerate(machines, 1):
    print(f"{i}/{len(machines)}")

    if (result := find_cheapest_way(ax, ay, 0, bx, by, 0, px, py)) != math.inf:
        part_1 += result

print(part_1)
