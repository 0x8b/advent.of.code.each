import pathlib
from collections import deque
from itertools import chain

from utils import *

data = pathlib.Path("../../data/2016/08.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

screen = [[" "] * 50 for _ in range(6)]


for line in lines:
    match line.split(" "):
        case ["rect", size]:
            w, h = size.split("x")

            for r in range(int(h)):
                for c in range(int(w)):
                    screen[r][c] = "#"

        case ["rotate", "row", y, "by", rot]:
            rotated = deque(screen[int(y[2:])])
            rotated.rotate(int(rot))

            screen[int(y[2:])] = list(rotated)

        case ["rotate", "column", x, "by", rot]:
            rotated = deque([screen[y][int(x[2:])] for y in range(6)])
            rotated.rotate(int(rot))

            for y, value in enumerate(rotated):
                screen[y][int(x[2:])] = value


part_1 = list(chain.from_iterable(screen)).count("#")

print(part_1)
print_matrix(screen)  # part_2
