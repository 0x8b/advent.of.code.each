import pathlib

from utils import *

data = pathlib.Path("../../data/2024/10.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

topo = matrix(lines, separator="", try_parse=True)


def find_trailheads(topo):
    return {
        (row, col)
        for row in range(len(topo))
        for col in range(len(topo[0]))
        if topo[row][col] == 0
    }


def count_all_trails(topo, trailhead_row, trailhead_col):
    rows = len(topo)
    cols = len(topo[0])

    trails = []

    def traverse(row, col, height, trail):
        if not (0 <= row < rows and 0 <= col < cols):
            return 0

        if topo[row][col] != height:
            return 0

        if height == 9:
            trails.append(trail)
            return 1

        return sum(
            traverse(row + dr, col + dc, height + 1, trail + [(row + dr, col + dc)])
            for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]
        )

    traverse(trailhead_row, trailhead_col, 0, [(trailhead_row, trailhead_col)])

    return trails


def count_trails(topo, distinct=False):
    count = 0

    for trailhead_row, trailhead_col in find_trailheads(topo):
        trails = count_all_trails(topo, trailhead_row, trailhead_col)

        if distinct:
            count += len(set(trail[-1] for trail in trails))
        else:
            count += len(trails)

    return count


part_1 = count_trails(topo, distinct=True)
part_2 = count_trails(topo)

print(part_1)
print(part_2)
