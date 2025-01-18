import pathlib
import re
from collections import defaultdict
from copy import deepcopy
from graphlib import TopologicalSorter

from utils import *

data = pathlib.Path("../../data/2017/07.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")


graph = defaultdict(list)
weights = dict()
stacks = dict()


for line in lines:
    disc, weight, *discs = re.sub(r"[)(,>\-]", "", line).split()

    weights[disc] = int(weight)

    for d in discs:
        graph[d].append(disc)

    stacks[disc] = discs


topological_sorter = TopologicalSorter(graph)

topological_order = list(topological_sorter.static_order())

part_1 = topological_order[0]

print(part_1)

original_weights = deepcopy(weights)

for disc in reversed(topological_order):
    w = [weights[d] for d in stacks[disc]]

    if sum(w[: len(w) // 2]) != sum(w[-1 * (len(w) // 2) :]):
        part_2 = original_weights[stacks[disc][w.index(max(w))]] - (max(w) - min(w))

        print(part_2)

        break

    weights[disc] += sum(w)
