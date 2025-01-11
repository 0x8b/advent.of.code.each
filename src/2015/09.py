import math
import pathlib
from collections import defaultdict
from itertools import permutations

data = pathlib.Path("../../data/2015/09.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

distances = dict()
nodes = set()

for line in lines:
    a, _, b, _, distance = line.split(" ")

    distances[a, b] = int(distance)
    distances[b, a] = int(distance)

    nodes.update({a, b})


part_1 = math.inf
part_2 = 0

for permutation in permutations(nodes):
    try:
        distance = sum(distances[a, b] for a, b in zip(permutation, permutation[1:]))

        part_1 = min(part_1, distance)
        part_2 = max(part_2, distance)
    except Exception:
        pass

print(part_1)
print(part_2)
