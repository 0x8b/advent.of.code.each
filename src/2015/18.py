import pathlib
from copy import deepcopy
from itertools import chain

from utils import *

data = pathlib.Path("../../data/2015/18.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

grid = matrix(lines, separator="")

rows, cols = len(grid), len(grid[0])

PART_2 = False

for step in range(100):
    next_grid = deepcopy(grid)

    for row in range(rows):
        for col in range(cols):
            neighbors = []

            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if (dr, dc) == (0, 0):
                        continue

                    r, c = row + dr, col + dc

                    if 0 <= r < rows and 0 <= c < cols:
                        neighbors.append(grid[r][c])

            if grid[row][col] == "#":
                next_grid[row][col] = "#" if neighbors.count("#") in [2, 3] else "."
            else:
                next_grid[row][col] = "#" if neighbors.count("#") == 3 else "."

    grid = next_grid

    if PART_2:
        grid[0][0] = "#"
        grid[0][cols - 1] = "#"
        grid[rows - 1][0] = "#"
        grid[rows - 1][cols - 1] = "#"


answer = list(chain.from_iterable(grid)).count("#")

print(answer)  # part_1, part_2
