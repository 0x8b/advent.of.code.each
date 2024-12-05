import math
import pathlib
from graphlib import TopologicalSorter

data = pathlib.Path("../../data/2024/05.txt").read_text(encoding="utf-8")
rules, pages = data.strip().split("\n\n")

rules = [
    [int(n) for n in rule.split("|")] for rule in rules.split("\n")
]

pages = [
    [int(n) for n in page.split(",")] for page in pages.split("\n")
]

part_1 = 0
part_2 = 0

for order in pages:
    ts = TopologicalSorter()

    for rule in [
        rule for rule in rules if len(set(rule) & set(order)) == 2
    ]:
        ts.add(rule[1], rule[0])

    topological_order = list(ts.static_order())

    middle_index = math.floor(len(order) / 2)

    if order == topological_order:
        part_1 += order[middle_index]
    else:
        part_2 += topological_order[middle_index]

print(part_1)
print(part_2)
