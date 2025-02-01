import math
import pathlib
from collections import defaultdict

from utils import *

data = pathlib.Path("../../data/2018/06.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

areas = dict()

for line in lines:
    col, row = line.split(",")

    areas[(int(row), int(col))] = 0

min_row, max_row = min(c[0] for c in areas), max(c[0] for c in areas)
min_col, max_col = min(c[1] for c in areas), max(c[1] for c in areas)


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


infinite = set()

for row in range(min_row, max_row + 1):
    for col in range(min_col, max_col + 1):
        closest_coords = []
        shortest_distance = math.inf

        for r, c in areas.keys():
            dist = distance((r, c), (row, col))

            if dist == shortest_distance:
                closest_coords.append((r, c))
            elif dist < shortest_distance:
                closest_coords = [(r, c)]
                shortest_distance = dist

        if len(closest_coords) == 1:
            areas[closest_coords[0]] += 1

            if row in [min_row, max_row] or col in [min_col, max_col]:
                infinite.add(closest_coords[0])

max_area = 0

for position, area in areas.items():
    if position not in infinite and area > max_area:
        max_area = area

print(max_area)  # part_1


part_2 = 0


for row in range(min_row, max_row + 1):
    for col in range(min_col, max_col + 1):
        total_distance = sum(distance((row, col), coords) for coords in areas.keys())

        if total_distance < 10_000:
            part_2 += 1

print(part_2)
