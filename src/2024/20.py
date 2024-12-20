import pathlib
from collections import Counter
from copy import deepcopy

import networkx
from utils import *

data = pathlib.Path("../../data/2024/20.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

racetrack = matrix(lines, separator="")

rows, cols = len(racetrack), len(racetrack[0])
cheats = set()

for row in range(rows):
    for col in range(cols):
        if racetrack[row][col] == "S":
            start_row, start_col = row, col
            racetrack[row][col] = "."

        if racetrack[row][col] == "E":
            end_row, end_col = row, col
            racetrack[row][col] = "."

        if racetrack[row][col] == "#":
            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_row, new_col = row + dr, col + dc

                if 0 <= new_row < rows and 0 <= new_col < cols:
                    if racetrack[new_row][new_col] == ".":
                        cheats.add((row, col))


def build_graph(racetrack):
    edges = []
    rows, cols = len(racetrack), len(racetrack[0])

    for row in range(rows):
        for col in range(cols):
            if racetrack[row][col] == ".":
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    nr, nc = row + dr, col + dc

                    if 0 <= nr < rows and 0 <= nc < cols:
                        if racetrack[nr][nc] == ".":
                            edges.append(((row, col), (nr, nc)))

    graph = networkx.Graph(edges)

    return graph


RACETRACK = deepcopy(racetrack)

shortest_distance_without_cheating = networkx.shortest_path_length(
    build_graph(RACETRACK), (start_row, start_col), (end_row, end_col)
)

shortest_distances = []

for i, cheat in enumerate(cheats):
    print(f"{i}/{len(cheats)}")
    racetrack = deepcopy(RACETRACK)

    cheat_row, cheat_col = cheat

    racetrack[cheat_row][cheat_col] = "."

    shortest_distances.append(
        networkx.shortest_path_length(
            build_graph(racetrack), (start_row, start_col), (end_row, end_col)
        )
    )

counter = Counter(
    [shortest_distance_without_cheating - distance for distance in shortest_distances]
)

part_1 = sum(
    num_of_cheats
    for picoseconds, num_of_cheats in counter.items()
    if picoseconds >= 100
)

print(part_1)
