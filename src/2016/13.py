import pathlib

import networkx
from utils import *

data = pathlib.Path("../../data/2016/13.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

favourite_number = int(lines[0])

rows, cols = 100, 100

grid = [["."] * cols for _ in range(rows)]

for y in range(rows):
    for x in range(cols):
        if (
            x * x + 3 * x + 2 * x * y + y + y * y + favourite_number
        ).bit_count() % 2 == 1:
            grid[y][x] = "#"

edges = []

for row in range(rows):
    for col in range(cols):
        for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            if 0 <= row + dr < rows and 0 <= col + dc < cols:
                if (dr, dc) == (0, 0):
                    continue

                if grid[row][col] == "." and grid[row + dr][col + dc] == ".":
                    edges.append(((row, col), (row + dr, col + dc)))


graph = networkx.Graph(edges)

shortest_path_length = networkx.shortest_path_length(graph, (1, 1), (39, 31))

part_1 = shortest_path_length

print(part_1)

part_2 = 0

for row in range(rows):
    for col in range(cols):
        if grid[row][col] == "#":
            continue

        try:
            shortest_path_length = networkx.shortest_path_length(
                graph, (1, 1), (row, col)
            )

            part_2 += int(shortest_path_length <= 50)
        except (
            networkx.exception.NodeNotFound,
            networkx.exception.NetworkXNoPath,
        ) as exc:

            pass

print(part_2)
