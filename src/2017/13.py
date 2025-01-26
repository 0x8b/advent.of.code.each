import pathlib
from collections import defaultdict
from itertools import cycle, islice

from utils import *

data = pathlib.Path("../../data/2017/13.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")


def security_scanner(r):
    if r == 0:
        return None

    def gen(r):
        while True:
            yield from range(r)
            yield from range(r, 0, -1)

    return gen(r - 1)


puzzle = defaultdict(int)

for line in lines:
    depth, range_area = line.split(":")

    puzzle[int(depth.strip())] = int(range_area.strip())


firewall = [security_scanner(puzzle[depth]) for depth in range(max(puzzle.keys()) + 1)]

values = [None if v is None else next(v) for v in firewall]

severity = 0

for packet_index in range(len(firewall)):
    if values[packet_index] == 0:
        severity += packet_index * puzzle[packet_index]
        caught = True

    values = [None if v is None else next(v) for v in firewall]


part_1 = severity

print(part_1)


def g(n):
    while True:
        if n == 0:
            yield 1
        else:
            yield 0

            for _ in range(2 * (n - 1) - 1):
                yield 1


generators = [
    islice(cycle(g(puzzle[depth])), depth, None)
    for depth in range(max(puzzle.keys()) + 1)
]

m = max(puzzle.keys()) + 1

for delay in range(60_000_000):
    if sum(next(g) for g in generators) >= m:
        print(delay)  # part_2
        break
