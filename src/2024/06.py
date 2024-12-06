import pathlib
from collections import defaultdict

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

direction = "up"

direction_change = {
    "up": "right",
    "right": "down",
    "down": "left",
    "left": "up",
}

vectors = {
    "up": {"row": -1, "col": 0},
    "right": {"row": 0, "col": 1},
    "down": {"row": 1, "col": 0},
    "left": {"row": 0, "col": -1},
}


def calculate(puzzle, guard_row, guard_col):
    direction = "up"

    visited = defaultdict(int)
    visited[(guard_row, guard_col)] += 1

    trace = [(guard_row, guard_col)]

    while True:
        try:
            if (
                puzzle[guard_row + vectors[direction]["row"]][
                    guard_col + vectors[direction]["col"]
                ]
                == "#"
            ):
                direction = direction_change[direction]
            else:
                guard_row = guard_row + vectors[direction]["row"]
                guard_col = guard_col + vectors[direction]["col"]

                current_guard_position = (guard_row, guard_col)

                visited[current_guard_position] += 1

                trace.append(current_guard_position)

                if visited[current_guard_position] > 10:
                    return {
                        "visited": visited,
                        "cycle": False,
                    }

                if trace.count(current_guard_position) > 1:
                    last_index = len(trace) - 1
                    penultimate_index = trace.index(
                        trace[last_index], 0, last_index - 1
                    )
                    length = last_index - penultimate_index

                    if (
                        trace[penultimate_index - length + 1 : penultimate_index + 1]
                        == trace[penultimate_index + 1 : last_index + 1]
                    ):
                        return {
                            "visited": visited,
                            "cycle": True,
                        }

        except Exception:
            break

    return {
        "visited": visited,
        "cycle": False,
    }


part_1 = len(
    list(
        value
        for value in calculate(puzzle, guard_row, guard_col).get("visited").values()
        if value != 0
    )
)

print(part_1)

part_2 = 0

for row in range(len(puzzle)):
    for col in range(len(puzzle[0])):
        print((row, col))

        if row == guard_row and col == guard_col:
            continue

        if puzzle[row][col] == ".":
            cloned_puzzle = [[c for c in r] for r in puzzle]
            cloned_puzzle[row][col] = "#"

            if calculate(cloned_puzzle, guard_row, guard_col).get("cycle"):
                print("CYCLE", (row, col))

                part_2 += 1

                print("TOTAL", part_2)

print(part_2)  # 962 too low; 2252 too high
