import pathlib

import networkx

data = pathlib.Path("../../data/2024/23.txt").read_text(encoding="utf-8")
connections = [tuple(line.split("-")) for line in data.strip().split("\n")]

part_1 = 0
part_2 = ""

max_clique_size = 0

for clique in networkx.enumerate_all_cliques(networkx.Graph(connections)):
    if len(clique) == 3:
        part_1 += any(host.startswith("t") for host in clique)

    if len(clique) > max_clique_size:
        max_clique_size = len(clique)

        part_2 = ",".join(sorted(clique))

print(part_1)
print(part_2)
