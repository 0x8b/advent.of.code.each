import pathlib
from collections import defaultdict
from itertools import permutations

from utils import *

data = pathlib.Path("../../data/2015/13.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

happiness = defaultdict(int)
people = set()

for line in lines:
    person_1, gain_or_lose, points, person_2 = (
        line.replace("would ", "")
        .replace("happiness units by sitting next to ", "")
        .replace(".", "")
        .split(" ")
    )

    happiness[person_1, person_2] = (
        int(points) if gain_or_lose == "gain" else -1 * int(points)
    )

    people.update({person_1, person_2})

max_happiness = 0

for permutation in permutations(people):
    try:
        max_happiness = max(
            max_happiness,
            sum(
                happiness[person_1, person_2] + happiness[person_2, person_1]
                for person_1, person_2 in zip(permutation, permutation[1:])
            )
            + happiness[permutation[-1], permutation[0]]
            + happiness[permutation[0], permutation[-1]],
        )

    except Exception:
        pass

print(max_happiness)  # part_1

for person in people:
    happiness[person, "me"] = 0
    happiness["me", person] = 0

people.add("me")

max_happiness = 0

for permutation in permutations(people):
    try:
        max_happiness = max(
            max_happiness,
            sum(
                happiness[person_1, person_2] + happiness[person_2, person_1]
                for person_1, person_2 in zip(permutation, permutation[1:])
            )
            + happiness[permutation[-1], permutation[0]]
            + happiness[permutation[0], permutation[-1]],
        )

    except Exception:
        pass

print(max_happiness)  # part_2
