import pathlib
from itertools import combinations

from utils import *

data = pathlib.Path("../../data/2024/08.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

puzzle = matrix(lines, separator="")


def find_antinodes(a, b, cols, rows, is_ray=False):
    antinodes = set()

    dr = a[0] - b[0]
    dc = a[1] - b[1]

    a = list(a)
    b = list(b)

    while True:
        a[0] = a[0] + dr
        a[1] = a[1] + dc

        if 0 <= a[0] < rows and 0 <= a[1] < cols:
            antinodes.add((a[0], a[1]))
        else:
            break

        if not is_ray:
            break

    while True:
        b[0] = b[0] - dr
        b[1] = b[1] - dc

        if 0 <= b[0] < rows and 0 <= b[1] < cols:
            antinodes.add((b[0], b[1]))
        else:
            break

        if not is_ray:
            break

    return antinodes


def find_antennas(puzzle, frequency):
    antennas = set()

    for row in range(len(puzzle)):
        for col in range(len(puzzle[0])):
            if puzzle[row][col] == frequency:
                antennas.add((row, col))

    return antennas


def count_antinodes_by_frequency(puzzle, frequency, is_part_2):
    rows = len(puzzle)
    cols = len(puzzle[0])

    antennas = find_antennas(puzzle, frequency)

    antinodes = set()

    if is_part_2:
        antinodes = antinodes.union(antennas)

    for [a, b] in combinations(antennas, 2):
        antinodes = antinodes.union(find_antinodes(a, b, rows, cols, is_ray=is_part_2))

    return antinodes


def count_antinodes(puzzle, is_part_2=False):
    frequencies = set("".join("".join([str(c) for c in row]) for row in puzzle))

    frequencies.remove(".")

    antinodes = set()

    for frequency in frequencies:
        antinodes = antinodes.union(
            count_antinodes_by_frequency(puzzle, frequency, is_part_2=is_part_2)
        )

    return len(antinodes)


part_1 = count_antinodes(puzzle)
part_2 = count_antinodes(puzzle, is_part_2=True)

print(part_1)
print(part_2)
