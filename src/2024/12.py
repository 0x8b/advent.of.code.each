import pathlib
from collections import deque

from utils import *

data = pathlib.Path("../../data/2024/12.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

garden = matrix(lines, separator="")

rows = len(garden)
cols = len(garden[0])

coords = set((row, col) for row in range(rows) for col in range(cols))

regions = []

while len(coords):
    first = coords.pop()

    region_name = garden[first[0]][first[1]]

    queue = deque()
    queue.append(first)

    region = set()
    region.add(first)

    while len(queue):
        row, col = queue.popleft()

        for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            nr, nc = row + dr, col + dc

            if (
                0 <= nr < rows
                and 0 <= nc < cols
                and garden[nr][nc] == region_name
                and (nr, nc) not in region
            ):
                queue.append((nr, nc))
                region.add((nr, nc))
                coords.remove((nr, nc))

    regions.append((region_name, region))


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

for region_name, region in regions:
    part_1 += calculate_area(region) * calculate_perimeter(region)

print(part_1)


def count_segments(cut_segments):
    cut_segments = sorted(cut_segments)

    segments = [[cut_segments.pop(0)]]

    for s in cut_segments:
        if segments[-1][-1] + 1 == s:
            segments[-1].append(s)
        else:
            segments.append([s])

    return len(segments)


def count_sides(region):
    edges = set()

    for row, col in region:
        for side, dr, dc in [["t", -1, 0], ["r", 0, 1], ["b", 1, 0], ["l", 0, -1]]:
            nr, nc = row + dr, col + dc

            if (nr, nc) not in region:
                edges.add((side, row, col))

    sides = 0

    while len(edges):
        first = edges.pop()

        cut_segments = set([first]) | set(
            (side, row, col)
            for side, row, col in edges
            if side == first[0]
            and (
                (first[0] in "tb" and row == first[1])
                or (first[0] in "rl" and col == first[2])
            )
        )

        sides += count_segments(
            [col if side in "tb" else row for (side, row, col) in cut_segments]
        )

        for s in cut_segments:
            edges.discard(s)

    return sides


part_2 = 0

for _, region in regions:
    part_2 += calculate_area(region) * count_sides(region)

print(part_2)
