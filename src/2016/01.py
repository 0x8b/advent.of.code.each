import pathlib

path = (
    pathlib.Path("../../data/2016/01.txt")
    .read_text(encoding="utf-8")
    .strip()
    .split(", ")
)

path = [(a[:1], int(a[1:])) for a in path]

bunny_x, bunny_y = 0, 0

seen = set((bunny_x, bunny_y))

directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]
direction = 0

part_2 = None

for turn, steps in path:
    if turn == "R":
        direction = (direction + 1 + 4) % 4
    elif turn == "L":
        direction = (direction - 1 + 4) % 4

    for s in range(steps):
        bunny_x, bunny_y = (
            bunny_x + directions[direction][0],
            bunny_y + directions[direction][1],
        )

        if part_2 is None and (bunny_x, bunny_y) in seen:
            part_2 = abs(bunny_x) + abs(bunny_y)
        else:
            seen.add((bunny_x, bunny_y))

part_1 = abs(bunny_x) + abs(bunny_y)

print(part_1)
print(part_2)
