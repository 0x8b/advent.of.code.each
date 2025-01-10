import pathlib
from collections import defaultdict

from utils import *

data = pathlib.Path("../../data/2017/03.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

puzzle = int(lines[0])


def spiral():
    loop_start_x, loop_start_y = 1, 1
    size = 3

    while True:
        for dy in range(size - 2):
            x, y = loop_start_x, loop_start_y - 1 - dy
            yield x, y

        for dx in range(size):
            x, y = loop_start_x - dx, loop_start_y - size + 1
            yield x, y

        for dy in range(size - 2):
            x, y = loop_start_x - size + 1, loop_start_y - size + 2 + dy
            yield x, y

        for dx in range(size):
            x, y = loop_start_x - size + 1 + dx, loop_start_y
            yield x, y

        loop_start_x += 1
        loop_start_y += 1
        size += 2


for value, (x, y) in enumerate(spiral(), 2):
    if value == puzzle:
        part_1 = abs(x) + abs(y)

        print(part_1)

        break


grid = defaultdict(int)
grid[0, 0] = 1


for x, y in spiral():
    value = sum(
        grid[x + dx, y + dy]
        for dx in [-1, 0, 1]
        for dy in [-1, 0, 1]
        if (dx, dy) != (0, 0)
    )

    grid[x, y] = value

    if value > puzzle:
        part_2 = value

        print(part_2)

        break
