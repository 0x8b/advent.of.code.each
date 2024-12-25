import pathlib

from utils import *

data = pathlib.Path("../../data/2024/25.txt").read_text(encoding="utf-8")
schematics = [
    [list(line) for line in lines.split("\n")] for lines in data.strip().split("\n\n")
]

locks = []
keys = []

for schematic in schematics:
    pin = [col.count("#") - 1 for col in zip(*schematic)]

    locks.append(pin) if schematic[0][0] == "#" else keys.append(pin)

part_1 = 0

for key in keys:
    for lock in locks:
        part_1 += all(k + l <= 5 for k, l in zip(key, lock))

print(part_1)
