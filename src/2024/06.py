import pathlib

from utils import *

data = pathlib.Path("../../data/2024/06.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

puzzle = matrix(lines, separator="", try_parse=True)

guard_row, guard_col = 0, 0


for i, row in enumerate(puzzle):
    try:
        guard_col = row.index("^")
        guard_row = i
    except Exception:
        pass

visited = {(guard_row, guard_col)}
direction = "up"

direction_change = {
    "up": "right",
    "right": "down",
    "down": "left",
    "left": "up",
}

vectors = {
    "up": [-1, 0],
    "right": [0, 1],
    "down": [1, 0],
    "left": [0, -1],
}

while True:
    try:
        if (
            puzzle[guard_row + vectors[direction][0]][guard_col + vectors[direction][1]]
            == "#"
        ):
            direction = direction_change[direction]
        else:
            guard_row = guard_row + vectors[direction][0]
            guard_col = guard_col + vectors[direction][1]

            visited.add((guard_row, guard_col))
    except Exception:
        break

part_1 = len(visited)

print(part_1)
