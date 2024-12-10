import pathlib

from utils import *

data = pathlib.Path("../../data/2024/10.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

topographic_map = matrix(lines, separator="", try_parse=True)


def find_trailheads(topographic_map):
    return {
        (row, col)
        for row in range(len(topographic_map))
        for col in range(len(topographic_map[0]))
        if topographic_map[row][col] == 0
    }


def count_paths(topographic_map, trailhead_row, trailhead_col):
    rows = len(topographic_map)
    cols = len(topographic_map[0])

    traces = []

    def traverse(row, col, height, trace):
        if not (0 <= row < rows and 0 <= col < cols):
            return 0

        if height == 9:
            traces.append(trace)
            return 1

        return sum(
            traverse(row + dr, col + dc, height + 1, trace + [(row + dr, col + dc)])
            for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]
            if 0 <= row + dr < rows
            and 0 <= col + dc < cols
            and topographic_map[row + dr][col + dc] == height + 1
        )

    traverse(trailhead_row, trailhead_col, 0, [(trailhead_row, trailhead_col)])

    return traces


def count_trails(topographic_map, distinct=False):
    count = 0

    for trailhead_row, trailhead_col in find_trailheads(topographic_map):
        traces = count_paths(topographic_map, trailhead_row, trailhead_col)

        if distinct:
            count += len(set(trace[-1] for trace in traces))
        else:
            count += len(traces)

    return count


part_1 = count_trails(topographic_map, distinct=True)
part_2 = count_trails(topographic_map)

print(part_1)
print(part_2)
