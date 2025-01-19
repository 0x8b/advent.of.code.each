import pathlib
import networkx

from utils import *

data = pathlib.Path("../../data/2017/12.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

edges = []
remaining = set()

for line in lines:
    program, *programs = ints(line)

    for p in programs:
        edges.append((program, p))

    remaining.add(program)
    remaining.update(programs)


graph = networkx.Graph(edges)

part_1 = len(networkx.descendants(graph, 122) | {122})

set_sizes = []

print(part_1)


while remaining:
    program = remaining.pop()

    descendants = networkx.descendants(graph, program)

    remaining.difference_update(descendants | {program})

    set_sizes.append(len(descendants) + 1)


part_2 = len(set_sizes)

print(part_2)
