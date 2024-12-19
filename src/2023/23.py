import pathlib
import string

import networkx
from utils import *

data = pathlib.Path("../../data/2023/23.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

map = matrix(lines, separator="")

rows, cols = len(map), len(map[0])

dag_edges = set()

for row in range(rows):
    for col in range(cols):
        for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < rows and 0 <= new_col < cols:
                if map[row][col] == ">":
                    if map[row][col + 1] == ".":
                        dag_edges.add(((row, col), (row, col + 1)))
                    if map[row][col - 1] == ".":
                        dag_edges.add(((row, col - 1), (row, col)))

                if map[row][col] == "<":
                    if map[row][col - 1] == ".":
                        dag_edges.add(((row, col), (row, col - 1)))
                    if map[row][col + 1] == ".":
                        dag_edges.add(((row, col + 1), (row, col)))

                if map[row][col] == "v":
                    if map[row + 1][col] == ".":
                        dag_edges.add(((row, col), (row + 1, col)))
                    if map[row - 1][col] == ".":
                        dag_edges.add(((row - 1, col), (row, col)))

                if map[row][col] == "^":
                    if map[row + 1][col] == ".":
                        dag_edges.add(((row + 1, col), (row, col)))
                    if map[row - 1][col] == ".":
                        dag_edges.add(((row, col), (row - 1, col)))

remaining_dag_edges = set()


def find_next_edge(prev_node, next_node):
    seen = set()
    seen.add(prev_node)

    def rec(node):
        seen.add(node)

        row, col = node

        if map[row][col] != ".":
            return

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = row + dr, col + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                if (nr, nc) in seen:
                    continue

                if map[nr][nc] == ".":
                    remaining_dag_edges.add((node, (nr, nc)))
                    rec((nr, nc))

    rec(next_node)


# for i, (prev_node, next_node) in enumerate(dag_edges):
#     if map[next_node[0]][next_node[1]] == ".":
#         find_next_edge(prev_node, next_node)

# find_next_edge((-1, 1), (0, 1))

for prev_node, next_node in remaining_dag_edges:
    # print(prev_node, next_node)
    map[prev_node[0]][prev_node[1]] = "o"
    map[next_node[0]][next_node[1]] = "o"

for prev_node, next_node in dag_edges:
    print(prev_node, next_node)
    map[prev_node[0]][prev_node[1]] = "█"
    map[next_node[0]][next_node[1]] = "█"

print_matrix(map)

dag_edges.update(remaining_dag_edges)

graph = networkx.Graph(dag_edges)

print(graph)

print(networkx.is_directed_acyclic_graph(graph))

cycle = networkx.find_cycle(graph)

print(cycle)

# print(networkx.dag_longest_path(graph))
