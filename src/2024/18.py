import pathlib
from itertools import batched

import networkx
from utils import *

data = pathlib.Path("../../data/2024/18.txt").read_text(encoding="utf-8")

rows, cols = 71, 71


grid = [["." for x in range(cols)] for y in range(rows)]

first_bytes = 1024
bytes = list(batched(ints(data), 2))

for col, row in bytes[:first_bytes]:
    grid[row][col] = "#"


def shortest_path_length(grid):
    edges = []

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == ".":
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    if 0 <= row + dr < rows and 0 <= col + dc < cols:
                        if grid[row + dr][col + dc] == ".":
                            edges.append(((row, col), (row + dr, col + dc), 1))

    graph = networkx.Graph()

    graph.add_weighted_edges_from(edges)

    return networkx.shortest_path_length(graph, (0, 0), (rows - 1, cols - 1))


part_1 = shortest_path_length(grid)

print(part_1)

for gcol, grow in bytes[1024:]:
    grid[grow][gcol] = "#"

    try:
        shortest_path_length(grid)
    except Exception:
        part_2 = f"{gcol},{grow}"

        print(part_2)
        break
