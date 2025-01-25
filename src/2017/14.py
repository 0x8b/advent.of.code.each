import pathlib
from collections import deque
from functools import reduce
from itertools import batched, chain

from utils import *

data = pathlib.Path("../../data/2017/14.txt").read_text(encoding="utf-8")

key = data.strip()


def knot_hash(string):
    lenghts = [ord(s) for s in string] + [17, 31, 73, 47, 23]
    sparse_hash = list(range(256))
    skip = 0
    current_position = 0

    for _ in range(64):
        for length in lenghts:
            indices = [(current_position + i) % len(sparse_hash) for i in range(length)]

            values = list(reversed([sparse_hash[i] for i in indices]))

            for i, v in enumerate(values):
                sparse_hash[indices[i]] = v

            current_position = (current_position + length + skip) % len(sparse_hash)
            skip += 1

    dense_hash = "".join(
        [
            hex(reduce(lambda a, b: a ^ b, seq))[2:].zfill(2)
            for seq in batched(sparse_hash, 16)
        ]
    )

    return dense_hash


grid = []

for row in range(128):
    binary = "".join(bin(int(ch, 16))[2:].zfill(4) for ch in knot_hash(f"{key}-{row}"))

    grid.append([int(v) for v in binary])

part_1 = list(chain.from_iterable(grid)).count(1)

print(part_1)


def get_group(grid, node):
    group = set([node])

    queue = deque([node])

    while queue:
        row, col = queue.popleft()

        for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            if 0 <= row + dr < len(grid) and 0 <= col + dc < len(grid[0]):
                adjacent_node = (row + dr, col + dc)

                if (
                    grid[adjacent_node[0]][adjacent_node[1]] == 1
                    and adjacent_node not in group
                ):
                    group.add(adjacent_node)
                    queue.append(adjacent_node)

    return group


used = set()

for row in range(128):
    for col in range(128):
        if grid[row][col] == 1:
            used.add((row, col))

part_2 = 0

while len(used):
    used.difference_update(get_group(grid, used.pop()))

    part_2 += 1

print(part_2)
