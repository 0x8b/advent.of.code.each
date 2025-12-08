import math
import operator
import pathlib

from utils import *

data = pathlib.Path("../../data/2025/08.txt").read_text(encoding="utf-8")

data = [tuple(row) for row in matrix(data, separator=",", try_parse=True)]


def distance(vec_1, vec_2):
    return int(sum(math.pow(p - q, 2) for p, q in zip(vec_1, vec_2)))


distances = {
    tuple(sorted([a, b])): distance(a, b) for a in data for b in data if a != b
}

distances = sorted(distances.items(), key=operator.itemgetter(1))

circuits = [set([c]) for c in data]

iteration = 0
while len(circuits) != 1:
    [a, b], _ = distances.pop(0)

    iteration += 1

    ai = find_index(circuits, lambda c: a in c)
    bi = find_index(circuits, lambda c: b in c)

    if ai < 0 or bi < 0:
        continue

    if ai != bi:
        circuits[ai] = circuits[ai].union(circuits[bi])
        circuits.pop(bi)

    if iteration == 1000:
        sizes = list(sorted([len(c) for c in circuits]))
        print("PART 1:", sizes[-1] * sizes[-2] * sizes[-3])

    if len(circuits) == 1:
        print("PART 2:", a[0] * b[0])
