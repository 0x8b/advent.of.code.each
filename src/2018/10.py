import pathlib
from copy import deepcopy

from utils import *

data = pathlib.Path("../../data/2018/10.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

points = []

for line in lines:
    points.append(ints(line))


def calculate_bounding_rect(points):
    min_x = min(p[0] for p in points)
    max_x = max(p[0] for p in points)

    min_y = min(p[0] for p in points)
    max_y = max(p[0] for p in points)

    return abs(max_x - min_x) * abs(max_y - min_y)


def print_space(points):
    min_x = min(p[0] for p in points)
    min_y = min(p[1] for p in points)

    max_x = max(p[0] for p in points)
    max_y = max(p[1] for p in points)

    pts = set((p[0] - min_x, p[1] - min_y) for p in points)

    for y in range(max_y - min_y + 1):
        for x in range(max_x - min_x + 1):
            if (x, y) in pts:
                print("█", end="")
            else:
                print(" ", end="")

        print()


# min_area = calculate_bounding_rect(points)
# min_area_index = 0

# for i in range(1, 12_000):
#     for p in points:
#         p[0] += p[2]
#         p[1] += p[3]

#         area = calculate_bounding_rect(points)

#         if area < min_area:
#             min_area_index = i
#             min_area = area


for i in range(10238, 10242):
    print(f"{i}:")  # part_1
    print_space([[p[0] + i * p[2], p[1] + i * p[3]] for p in points])  # part_2
    print()
