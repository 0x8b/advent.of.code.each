import pathlib
from itertools import batched

from utils import *

data = pathlib.Path("../../data/2015/16.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

ticket_tape = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

aunts = []

for line in lines:
    things = dict(
        (thing, int(count))
        for thing, count in batched(
            line.replace(":", "").replace(",", "").split(" ")[2:], 2
        )
    )

    aunts.append(things)


for sue_id, things in enumerate(aunts, 1):
    if all(ticket_tape[thing] == count for thing, count in things.items()):
        print(sue_id)  # part_1
        break

for sue_id, things in enumerate(aunts, 1):
    for thing, count in things.items():
        if thing in ["cats", "trees"]:
            if ticket_tape[thing] >= count:
                break
        elif thing in ["pomeranians", "goldfish"]:
            if ticket_tape[thing] <= count:
                break
        else:
            if ticket_tape[thing] != count:
                break
    else:
        print(sue_id)  # part_2
        break
