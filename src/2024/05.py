import pathlib
from graphlib import TopologicalSorter

import utils

data = pathlib.Path("../../data/2024/05.txt").read_text(encoding="utf-8")
rules, pages = data.strip().split("\n\n")

rules = [utils.ints(rule) for rule in rules.split("\n")]
pages = [utils.ints(page) for page in pages.split("\n")]

part_1 = 0
part_2 = 0

for order in pages:
    ts = TopologicalSorter()

    for [predecessor, node] in [
        rule for rule in rules if len(set(rule) & set(order)) == 2
    ]:
        ts.add(node, predecessor)

    topological_order = list(ts.static_order())

    middle_page = topological_order[len(topological_order) >> 1]

    if order == topological_order:
        part_1 += middle_page
    else:
        part_2 += middle_page

print(part_1)
print(part_2)
