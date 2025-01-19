import pathlib

from utils import *

data = pathlib.Path("../../data/2017/11.txt").read_text(encoding="utf-8")
path = data.strip().split(",")

edges = []

x, y, z = 0, 0, 0

moves = {
    "n": (-1, 1, 0),
    "s": (1, -1, 0),
    "ne": (0, 1, -1),
    "sw": (0, -1, 1),
    "nw": (-1, 0, 1),
    "se": (1, 0, -1),
}

visited = set()

visited.add((x, y, z))

for step in path:
    x += moves[step][0]
    y += moves[step][1]
    z += moves[step][2]

    visited.add((x, y, z))

last_position = (x, y, z)

part_1 = max(map(abs, last_position))

print(part_1)

part_2 = max(max(map(abs, position)) for position in visited)

print(part_2)
