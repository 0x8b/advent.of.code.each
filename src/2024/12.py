import pathlib
from collections import deque

from utils import *

data = pathlib.Path("../../data/2024/12.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

GARDEN = matrix(lines, separator="")

ROWS = len(GARDEN)
COLS = len(GARDEN[0])

coords = set((row, col) for row in range(ROWS) for col in range(COLS))

REGIONS = []

while len(coords):
    first = coords.pop()

    region_name = GARDEN[first[0]][first[1]]

    queue = deque()
    queue.append(first)

    region = set()
    region.add(first)

    while len(queue):
        row, col = queue.popleft()

        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nr, nc = row + dr, col + dc

            if (
                0 <= nr < ROWS
                and 0 <= nc < COLS
                and GARDEN[nr][nc] == region_name
                and (nr, nc) not in region
            ):
                queue.append((nr, nc))
                region.add((nr, nc))
                coords.remove((nr, nc))

    REGIONS.append((region_name, region))


def calculate_area(region):
    return len(region)


def calculate_perimeter(region):
    perimeter = len(region) * 4

    for row, col in region:
        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nr, nc = row + dr, col + dc

            if (nr, nc) in region:
                perimeter -= 1

    return perimeter


part_1 = 0

for region_name, region in REGIONS:
    part_1 += calculate_area(region) * calculate_perimeter(region)

print(part_1)


def count_sides(region):
    edges = set()

    for row, col in region:
        for side, dr, dc in [["t", -1, 0], ["r", 0, 1], ["b", 1, 0], ["l", 0, -1]]:
            nr, nc = row + dr, col + dc

            if (nr, nc) not in region:
                edges.add((side, row, col))

    count = 0

    while len(edges):
        first_fragment = edges.pop()

        cut_sides = set([first_fragment]) | set(
            (side, row, col)
            for side, row, col in edges
            if side == first_fragment[0]
            and (
                (first_fragment[0] in "tb" and row == first_fragment[1])
                or (first_fragment[0] in "rl" and col == first_fragment[2])
            )
        )

        edges.difference_update(cut_sides)

        cut_sides = sorted(
            [col if side in "tb" else row for (side, row, col) in cut_sides]
        )

        sides = [[cut_sides.pop(0)]]

        for side_fragment in cut_sides:
            if sides[-1][-1] + 1 == side_fragment:
                sides[-1].append(side_fragment)
            else:
                sides.append([side_fragment])

        count += len(sides)

    return count


part_2 = 0

for _, region in REGIONS:
    part_2 += calculate_area(region) * count_sides(region)

print(part_2)
