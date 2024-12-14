import pathlib
from collections import defaultdict

data = pathlib.Path("../../data/2015/03.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

moves = list(lines[0])


visited = defaultdict(int)
visited_part_2 = defaultdict(int)

x_step = {"^": 0, ">": 1, "v": 0, "<": -1}
y_step = {"^": 1, ">": 0, "v": -1, "<": 0}

x, y = 0, 0

visited[(x, y)] += 1
visited_part_2[(x, y)] += 2

xp, yp = 0, 0
xq, yq = 0, 0

for i, move in enumerate(moves):
    x += x_step[move]
    y += y_step[move]

    visited[(x, y)] += 1

    if i % 2 == 0:
        xp += x_step[move]
        yp += y_step[move]

        visited_part_2[(xp, yp)] += 1
    else:
        xq += x_step[move]
        yq += y_step[move]

        visited_part_2[(xq, yq)] += 1

part_1 = len(visited.values())
part_2 = len(visited_part_2.values())

print(part_1)
print(part_2)
