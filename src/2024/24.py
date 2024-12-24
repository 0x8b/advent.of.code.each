import pathlib
from graphlib import TopologicalSorter

from utils import *

data = pathlib.Path("../../data/2024/24.txt").read_text(encoding="utf-8")
inputs, connections = data.strip().split("\n\n")

inputs = dict(
    (line.split(": ")[0], bool(int(line.split(": ")[1])))
    for line in inputs.strip().split("\n")
)

connections = list(
    tuple(
        line.replace(" -> ", " ").split(" ") for line in connections.strip().split("\n")
    )
)

outputs = dict((connection[3], connection[:3]) for connection in connections)

ts = TopologicalSorter()

for predecessor_0, op, predecessor_1, node in connections:
    ts.add(node, predecessor_0)
    ts.add(node, predecessor_1)

topological_order = list(ts.static_order())

results = dict()

for node in topological_order:
    if node in inputs:
        results[node] = inputs[node]
    elif node in outputs:
        match outputs[node]:
            case x, "AND", y:
                results[node] = results[x] and results[y]
            case x, "OR", y:
                results[node] = results[x] or results[y]
            case x, "XOR", y:
                results[node] = results[x] ^ results[y]

part_1 = int(
    "".join(
        map(
            lambda b: str(int(b[1])),
            reversed(
                sorted(item for item in results.items() if item[0].startswith("z"))
            ),
        )
    ),
    base=2,
)

print(part_1)
