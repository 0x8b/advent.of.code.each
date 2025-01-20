import pathlib
from itertools import chain

from utils import *

data = pathlib.Path("../../data/2017/21.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

rules = dict(tuple(line.split(" => ")) for line in lines)


def flip(grid):
    return [list(reversed(row)) for row in grid]


def rotate(grid, rotations=1):
    rotated = flip(transpose(grid))

    return rotated if rotations == 1 else rotate(rotated, rotations - 1)


def serialize(grid):
    return "/".join("".join(row) for row in grid)


def deserialize(serialized_grid):
    return matrix(serialized_grid.split("/"), separator="")


extended_rules = dict()

for key, value in rules.items():
    g = matrix(key.replace("/", "\n"), separator="")

    extended_rules[serialize(g)] = value
    extended_rules[serialize(rotate(g))] = value
    extended_rules[serialize(rotate(g, 2))] = value
    extended_rules[serialize(rotate(g, 3))] = value

    extended_rules[serialize(flip(g))] = value
    extended_rules[serialize(rotate(flip(g)))] = value
    extended_rules[serialize(rotate(flip(g), 2))] = value
    extended_rules[serialize(rotate(flip(g), 3))] = value


for iterations in [5, 18]:
    grid = matrix(".#.\n..#\n###", separator="")

    for i in range(iterations):
        size = len(grid)

        if size % 2 == 0:
            new_size = size * 3 // 2
            new_grid = [[None] * new_size for _ in range(new_size)]

            for x in range(size // 2):
                for y in range(size // 2):
                    g = "/".join(
                        "".join(grid[2 * y + yy][2 * x + xx] for xx in range(2))
                        for yy in range(2)
                    )

                    gg = deserialize(extended_rules[g])

                    for xx in range(3):
                        for yy in range(3):
                            new_grid[3 * y + yy][3 * x + xx] = gg[yy][xx]

            grid = new_grid

        elif size % 3 == 0:
            new_size = size * 4 // 3
            new_grid = [[None] * new_size for _ in range(new_size)]

            for x in range(size // 3):
                for y in range(size // 3):
                    g = "/".join(
                        "".join(grid[3 * y + yy][3 * x + xx] for xx in range(3))
                        for yy in range(3)
                    )

                    gg = deserialize(extended_rules[g])

                    for xx in range(4):
                        for yy in range(4):
                            new_grid[4 * y + yy][4 * x + xx] = gg[yy][xx]

            grid = new_grid

    answer = list(chain.from_iterable(grid)).count("#")

    print(answer)  # part_1, part_2
