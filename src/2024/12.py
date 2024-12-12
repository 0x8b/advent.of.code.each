import pathlib
from collections import deque

from utils import *

data = pathlib.Path("../../data/2024/12.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

garden = matrix(lines, separator="")

# print(garden)


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


def calc_perimeter(region):
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
    perimeter = calc_perimeter(region)

    part_1 += area * perimeter

print(part_1)


def count_consecutives(nums):
    nums = sorted(nums)

    d = [[nums.pop(0)]]

    for n in nums:
        if d[-1][-1] + 1 == n:
            d[-1].append(n)
        else:
            d.append([n])

    return len(d)


def calc_sides(region):
    edges = set()

    for row, col in region:
        for direction, dr, dc in [["t", -1, 0], ["r", 0, 1], ["b", 1, 0], ["l", 0, -1]]:
            nr, nc = row + dr, col + dc

            if (nr, nc) not in region:
                edges.add((direction, row, col))

    sides = 0

    while len(edges):
        seed = edges.pop()

        match seed:
            case "t", r, c:
                s = set(a for a in edges if a[0] == "t" and a[1] == r)
                s.add(("t", r, c))

                for m in s:
                    edges.discard(m)

                sides += count_consecutives([c for (_, _, c) in s])
            case "r", r, c:
                s = set(a for a in edges if a[0] == "r" and a[2] == c)
                s.add(("r", r, c))

                for m in s:
                    edges.discard(m)

                sides += count_consecutives([r for (_, r, _) in s])
            case "b", r, c:
                s = set(a for a in edges if a[0] == "b" and a[1] == r)
                s.add(("b", r, c))

                for m in s:
                    edges.discard(m)

                sides += count_consecutives([c for (_, _, c) in s])
            case "l", r, c:
                s = set(a for a in edges if a[0] == "l" and a[2] == c)
                s.add(("l", r, c))

                for m in s:
                    edges.discard(m)

                sides += count_consecutives([r for (_, r, _) in s])

    return sides


part_2 = 0
for region_name, region in regions:
    area = len(region)
    sides = calc_sides(region)
    part_2 += area * sides

print(part_2)
