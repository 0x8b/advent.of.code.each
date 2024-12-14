import pathlib


data = pathlib.Path("../../data/2015/01.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

instructions = [1 if ch == "(" else -1 for ch in list(lines[0])]

part_1 = sum(instructions)

print(part_1)

floor = 0

for position, instruction in enumerate(instructions, 1):
    floor += instruction

    if floor == -1:
        part_2 = position

        print(part_2)

        break
