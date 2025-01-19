import pathlib

from utils import *

data = pathlib.Path("../../data/2022/09.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

print(lines)


head = (0, 0)
tail = (0, 0)

tail_visited = set()

tail_visited.add(tail)

moves = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0),
    "R": (1, 0),
}

for line in lines:
    direction, distance = line.strip().split()

    for _ in range(int(distance)):
        old_head = head

        head = (head[0] + moves[direction][0], head[1] + moves[direction][1])

        if abs(head[0] - tail[0]) >= 2 or abs(head[1] - tail[1]) >= 2:
            tail = old_head

        tail_visited.add(tail)

part_1 = len(tail_visited)

print(part_1)


snail = [(0, 0)] * 10
tail_visited = {snail[-1]}

for line in lines:
    direction, distance = line.strip().split()

    for _ in range(int(distance)):
        snail[0] = (
            snail[0][0] + moves[direction][0],
            snail[0][1] + moves[direction][1],
        )

        for i in range(1, len(snail)):
            if (
                abs(snail[i - 1][0] - snail[i][0]) == 2
                and abs(snail[i - 1][1] - snail[i][1]) == 2
            ):
                snail[i] = (
                    snail[i - 1][0] + (1 if snail[i][0] > snail[i - 1][0] else -1),
                    snail[i - 1][1] + (1 if snail[i][1] > snail[i - 1][1] else -1),
                )

            elif abs(snail[i - 1][0] - snail[i][0]) == 2:
                snail[i] = (
                    snail[i - 1][0] + (1 if snail[i][0] > snail[i - 1][0] else -1),
                    snail[i - 1][1],
                )

            elif abs(snail[i - 1][1] - snail[i][1]) == 2:
                snail[i] = (
                    snail[i - 1][0],
                    snail[i - 1][1] + (1 if snail[i][1] > snail[i - 1][1] else -1),
                )

        tail_visited.add(snail[-1])


part_2 = len(tail_visited)

print(part_2)
