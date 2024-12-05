import pathlib
from collections import defaultdict

from utils import *

data = pathlib.Path("../../data/2023/02.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

games = {}

for game in lines:
    idenfitier, bag = game[5:].split(":")

    games[idenfitier] = [
        matrix(
            [cube.strip().split(" ") for cube in cubes.strip().split(",")],
            try_parse=True,
        )
        for cubes in bag.strip().split(";")
    ]


def is_possible(c):
    d = dict([list(reversed(p)) for p in c])

    return d.get("red", 0) <= 12 and d.get("green", 0) <= 13 and d.get("blue", 0) <= 14


part_1 = 0
part_2 = 0

for game_id, bag in games.items():
    if all(is_possible(s) for s in bag):
        part_1 += int(game_id)

    dd = defaultdict(int)

    for c in bag:
        for cc in c:
            if dd[cc[1]] < cc[0]:
                dd[cc[1]] = cc[0]

    part_2 += dd.get("red", 0) * dd.get("green", 0) * dd.get("blue")


print(part_1)
print(part_2)
