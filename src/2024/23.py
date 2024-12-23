import pathlib
import networkx

from utils import *

data = pathlib.Path("../../data/2024/23.txt").read_text(encoding="utf-8")
connections = [set(line.split("-")) for line in data.strip().split("\n")]

groups = set()

for connection in connections:
    a, b = list(connection)
    connected = [c for c in connections if a in c or b in c]
    not_seen = set()

    for c in connected:
        not_seen.update(c)

    not_seen.discard(a)
    not_seen.discard(b)

    for host in not_seen:
        if {a, host} in connected and {b, host} in connected:
            groups.add(",".join(list(sorted([a, b, host]))))

groups = list(groups)


part_1 = 0

for group in groups:
    if "t" in [group[0], group[3], group[6]]:
        part_1 += 1


print(part_1)


graph = networkx.Graph([tuple(connection) for connection in connections])

passwords = [
    ",".join(sorted(clique)) for clique in networkx.find_cliques_recursive(graph)
]

passwords.sort(key=len)

part_2 = passwords[-1]

print(part_2)
