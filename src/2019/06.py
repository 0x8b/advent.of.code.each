import pathlib

import networkx

from utils import *

data = pathlib.Path("../../data/2019/06.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

objects = set()
edges = []

for line in lines:
    o1, o2 = line.split(")")

    objects.add(o1)
    objects.add(o2)

    edges.append((o1, o2))


space = networkx.Graph(edges)

part_1 = sum(networkx.shortest_path_length(space, "COM", object) for object in objects)

print(part_1)


part_2 = networkx.shortest_path_length(space, "YOU", "SAN") - 2

print(part_2)
