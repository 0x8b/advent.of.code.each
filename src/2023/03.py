import itertools
import pathlib
import re

from utils import *

data = pathlib.Path("../../data/2023/03.txt").read_text(encoding="utf-8")
engine_schematic = data.strip().split("\n")

symbols = []
for row in range(len(engine_schematic)):
    for col in range(len(engine_schematic[0])):
        if (symbol := engine_schematic[row][col]) not in ".0123456789":
            symbols.append((symbol, row, col))

numbers = []
for r, row in enumerate(engine_schematic):
    for match in re.finditer(r"\d+", row):
        numbers.append(
            (int(match.group(0)), set(zip(itertools.cycle([r]), range(*match.span(0)))))
        )


def adjacent_positions(row, col):
    positions = set()

    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if [dr, dc] != [0, 0]:
                positions.add((row + dr, col + dc))

    return positions


part_1 = 0

symbol_adjacent_positions = set()

for _, row, col in symbols:
    symbol_adjacent_positions.update(adjacent_positions(row, col))

for part_number, part_number_span in numbers:
    if part_number_span & symbol_adjacent_positions:
        part_1 += part_number

print(part_1)

part_2 = 0

for symbol, row, col in symbols:
    if symbol != "*":
        continue

    symbol_adjacent_positions = adjacent_positions(row, col)

    part_numbers = [
        part_number
        for part_number, part_number_span in numbers
        if part_number_span & symbol_adjacent_positions
    ]

    if len(part_numbers) == 2:
        part_2 += part_numbers[0] * part_numbers[1]

print(part_2)
