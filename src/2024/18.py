import pathlib
from itertools import batched

import networkx
from utils import *

data = pathlib.Path("../../data/2024/18.txt").read_text(encoding="utf-8")

rows, cols = 71, 71
grid = [["." for x in range(cols)] for y in range(rows)]


def shortest_path_length(grid):
    edges = []
    rows, cols = len(grid), len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == ".":
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if (
                        0 <= row + dr < rows
                        and 0 <= col + dc < cols
                        and grid[row + dr][col + dc] == "."
                    ):
                        edges.append(((row, col), (row + dr, col + dc)))

    return networkx.shortest_path_length(
        networkx.Graph(edges), (0, 0), (rows - 1, cols - 1)
    )


bytes = list(batched(ints(data), 2))

for col, row in bytes[:1024]:
    grid[row][col] = "#"

print(shortest_path_length(grid))  # part_1

for col, row in bytes[1024:]:
    grid[row][col] = "#"

    try:
        shortest_path_length(grid)
    except networkx.NetworkXNoPath:
        print(f"{col},{row}")  # part_2
        break
