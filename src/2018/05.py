import math
import pathlib
import string

from utils import *

data = pathlib.Path("../../data/2018/05.txt").read_text(encoding="utf-8")
polymer = data.strip()


def reduce_polymer(polymer):
    while True:
        reactive = re.compile(
            "|".join(
                f"{ch}{ch.upper()}|{ch.upper()}{ch}" for ch in string.ascii_lowercase
            )
        )

        reduced = re.sub(reactive, "", polymer)

        if len(reduced) != len(polymer):
            polymer = reduced
        else:
            break

    return polymer


part_1 = len(reduce_polymer(polymer))

print(part_1)

shortest_polymer = math.inf

for unit in string.ascii_lowercase:
    shortest_polymer = min(
        shortest_polymer,
        len(reduce_polymer(data.strip().replace(unit, "").replace(unit.upper(), ""))),
    )

part_2 = shortest_polymer

print(part_2)
