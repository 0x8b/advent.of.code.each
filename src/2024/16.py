import pathlib

from networkx import Graph, all_shortest_paths, shortest_path_length
from utils import *

data = pathlib.Path("../../data/2024/16.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

maze = matrix(lines, separator="")

for row in range(len(maze)):
    for col in range(len(maze[0])):
        if maze[row][col] == "S":
            reindeer_row = row
            reindeer_col = col

        elif maze[row][col] == "E":
            end_tile_row = row
            end_tile_col = col

maze[reindeer_row][reindeer_col] = "."
maze[end_tile_row][end_tile_col] = "."

vec_to_dir = {
    (-1, 0): "north",
    (1, 0): "south",
    (0, 1): "east",
    (0, -1): "west",
}

edges = []

for row in range(len(maze)):
    for col in range(len(maze[0])):
        if maze[row][col] != ".":
            continue

        for direction in ["north", "south", "west", "east"]:
            if row != reindeer_row and col != reindeer_col:
                if direction == "north" and maze[row + 1][col] == "#":
                    continue

                if direction == "east" and maze[row][col - 1] == "#":
                    continue

            if direction == "south" and maze[row - 1][col] == "#":
                continue

            if direction == "west" and maze[row][col + 1] == "#":
                continue

            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                if maze[row + dr][col + dc] != ".":
                    continue

                neighbor_direction = vec_to_dir[(dr, dc)]

                if direction == "west" and neighbor_direction == "east":
                    continue

                if direction == "east" and neighbor_direction == "west":
                    continue

                if direction == "north" and neighbor_direction == "south":
                    continue

                if direction == "south" and neighbor_direction == "north":
                    continue

                edges.append(
                    (
                        (row, col, direction),
                        (row + dr, col + dc, neighbor_direction),
                        1 if direction == neighbor_direction else 1001,
                    )
                )

graph = Graph()

graph.add_weighted_edges_from(edges)

part_1 = shortest_path_length(
    graph,
    (reindeer_row, reindeer_col, "east"),
    (end_tile_row, end_tile_col, "east"),
    weight="weight",
)

print(part_1)

nodes = {
    (row, col)
    for path in all_shortest_paths(
        graph,
        (reindeer_row, reindeer_col, "east"),
        (end_tile_row, end_tile_col, "east"),
        weight="weight",
    )
    for row, col, _ in path
}

part_2 = len(nodes)

print(part_2)
