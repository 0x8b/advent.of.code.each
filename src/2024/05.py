import math
import pathlib
from graphlib import TopologicalSorter

data = pathlib.Path("../../data/2024/05.txt").read_text(encoding="utf-8")
parts = data.strip().split("\n\n")

rules = [[int(n) for n in line.split("|")] for line in parts[0].split("\n")]
orderings = [[int(n) for n in line.split(",")] for line in parts[1].split("\n")]


part_1 = 0

incorrectly_ordered = []

for ordering in orderings:
    new_rules = [rule for rule in rules if len(set(ordering) & set(rule)) > 0]

    for [a, b] in new_rules:
        try:
            ai = ordering.index(a)
            bi = ordering.index(b)
        except Exception:
            pass
        else:
            assert 0 <= ai < len(ordering)
            assert 0 <= bi < len(ordering)

            if ai > bi:
                incorrectly_ordered.append(ordering)
                break
    else:
        middle_value = ordering[math.floor(len(ordering) / 2)]
        part_1 += middle_value

print(part_1)


def fix_ordering(ordering):
    ts = TopologicalSorter()

    for rule in [rule for rule in rules if len(set(rule) & set(ordering)) > 1]:
        ts.add(rule[1], rule[0])

    order = list(ts.static_order())

    return order


part_2 = 0

for ordering in incorrectly_ordered:
    ordering = fix_ordering(ordering)

    middle_value = ordering[math.floor(len(ordering) / 2)]
    part_2 += middle_value

print(part_2)
