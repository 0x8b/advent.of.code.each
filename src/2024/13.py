import math
import pathlib
from functools import cache

from utils import *


data = pathlib.Path("../../data/2024/13.txt").read_text(encoding="utf-8")

machines = [ints(machine) for machine in data.strip().split("\n\n")]


@cache
def find_cheapest_way_naive(ax, ay, an, bx, by, bn, px, py):
    if px < 0 or py < 0:
        return math.inf

    if px == 0 and py == 0:
        return an * 3 + bn

    return min(
        find_cheapest_way_naive(ax, ay, an + 1, bx, by, bn, px - ax, py - ay),
        find_cheapest_way_naive(ax, ay, an, bx, by, bn + 1, px - bx, py - by),
    )


def find_cheapest_way_optimized(ax, ay, bx, by, px, py):
    a_presses = (by * px - bx * py) / (ax * by - ay * bx)
    b_presses = (px - ax * a_presses) / bx

    if a_presses % 1 == 0 and b_presses % 1 == 0:
        return 3 * a_presses + b_presses

    return None


part_1 = 0
part_2 = 0

for ax, ay, bx, by, px, py in machines:
    if result := find_cheapest_way_optimized(ax, ay, bx, by, px, py):
        part_1 += int(result)

    if result := find_cheapest_way_optimized(
        ax, ay, bx, by, px + 10000000000000, py + 10000000000000
    ):
        part_2 += int(result)

print(part_1)
print(part_2)
