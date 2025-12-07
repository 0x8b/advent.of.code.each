import pathlib

from utils import *

data = pathlib.Path("../../data/2025/07.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

part_1 = 0

start_index = lines[0].index("S")

beams = [0] * len(lines[0])
beams[start_index] = 1

for y in range(2, len(lines)):
    splitters = [i for i, c in enumerate(lines[y]) if c == "^"]

    for splitter_index in splitters:
        if beams[splitter_index] > 0:
            beams[splitter_index + 1] += beams[splitter_index]
            beams[splitter_index - 1] += beams[splitter_index]
            beams[splitter_index] = 0

            part_1 += 1

print(part_1)

part_2 = sum(beams)

print(part_2)
