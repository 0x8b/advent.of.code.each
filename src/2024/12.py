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
    seed = coords.pop()

    region_name = garden[seed[0]][seed[1]]

    queue = deque()
    queue.append(seed)

    region = set()
    region.add(seed)

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
    area = len(region)
    perimeter = calculate_perimeter(region)

    part_1 += area * perimeter

print(part_1)


def count_distinct_sides(nums):
    nums = sorted(nums)

    sides = [[nums.pop(0)]]

    for num in nums:
        if sides[-1][-1] + 1 == num:
            sides[-1].append(num)
        else:
            sides.append([num])

    return len(sides)


def count_sides(region):
    edges = set()

    for row, col in region:
        for side, dr, dc in [["t", -1, 0], ["r", 0, 1], ["b", 1, 0], ["l", 0, -1]]:
            nr, nc = row + dr, col + dc

            if (nr, nc) not in region:
                edges.add((side, row, col))

    sides = 0

    while len(edges):
        seed = edges.pop()

        match seed:
            case "t", r, c:
                s = set([("t", r, c)]) | set(
                    e for e in edges if e[0] == "t" and e[1] == r
                )

                sides += count_distinct_sides([c for (_, _, c) in s])
            case "r", r, c:
                s = set([("r", r, c)]) | set(
                    e for e in edges if e[0] == "r" and e[2] == c
                )

                sides += count_distinct_sides([r for (_, r, _) in s])
            case "b", r, c:
                s = set([("b", r, c)]) | set(
                    e for e in edges if e[0] == "b" and e[1] == r
                )

                sides += count_distinct_sides([c for (_, _, c) in s])
            case "l", r, c:
                s = set([("l", r, c)]) | set(
                    e for e in edges if e[0] == "l" and e[2] == c
                )

                sides += count_distinct_sides([r for (_, r, _) in s])

        for e in s:
            edges.discard(e)

    return sides


part_2 = 0

for _, region in regions:
    area = len(region)
    sides = count_sides(region)

    part_2 += area * sides

print(part_2)
