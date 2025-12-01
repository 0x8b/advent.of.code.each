import pathlib

from utils import *

data = pathlib.Path("../../data/2025/01.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

rotations = [(line[0], int(line[1:])) for line in lines]

part_1 = 0
state = 50

for direction, change in rotations:
    if direction == "R":
        state += change
        state %= 100
    elif direction == "L":
        state = (100 + state - (change % 100)) % 100

    part_1 += 1 if state == 0 else 0

print(part_1)
