import pathlib
from collections import defaultdict

data = pathlib.Path("../../data/2019/03.txt").read_text(encoding="utf-8")
first_wire, second_wire = data.strip().split("\n")

first_wire = [(item[0], int(item[1:])) for item in first_wire.strip().split(",")]
second_wire = [(item[0], int(item[1:])) for item in second_wire.strip().split(",")]


seen = set()

x, y = 0, 0

seen.add((x, y))

for direction, distance in first_wire:
    for step in range(distance):
        match direction:
            case "U":
                x, y = x, y + 1
            case "D":
                x, y = x, y - 1
            case "L":
                x, y = x - 1, y
            case "R":
                x, y = x + 1, y

        seen.add((x, y))


crossed = set()

x, y = 0, 0

for direction, distance in second_wire:
    for step in range(distance):
        match direction:
            case "U":
                x, y = x, y + 1
            case "D":
                x, y = x, y - 1
            case "L":
                x, y = x - 1, y
            case "R":
                x, y = x + 1, y

        if (x, y) in seen:
            crossed.add((x, y))

part_1 = min(abs(x) + abs(y) for x, y in crossed)

print(part_1)


distances = defaultdict(list)

x, y = 0, 0

steps = 0

for direction, distance in first_wire:
    for step in range(distance):
        match direction:
            case "U":
                x, y = x, y + 1
            case "D":
                x, y = x, y - 1
            case "L":
                x, y = x - 1, y
            case "R":
                x, y = x + 1, y

        steps += 1

        if (x, y) in crossed:
            distances[(x, y)].append(steps)

x, y = 0, 0

steps = 0

for direction, distance in second_wire:
    for step in range(distance):
        match direction:
            case "U":
                x, y = x, y + 1
            case "D":
                x, y = x, y - 1
            case "L":
                x, y = x - 1, y
            case "R":
                x, y = x + 1, y

        steps += 1

        if (x, y) in crossed:
            distances[(x, y)].append(steps)


part_2 = min(d[1][0] + d[1][1] for d in distances.items())

print(part_2)
