import pathlib

from utils import *

data = pathlib.Path("../../data/2022/08.txt").read_text(encoding="utf-8")

forest = matrix(data, separator="", try_parse=True)

rows, cols = len(forest), len(forest[0])

part_1 = 2 * cols + 2 * (rows - 2)

visible = set()

for row in range(1, rows - 1):
    h = forest[row][0]

    for col in range(1, cols - 1):
        if h < forest[row][col]:
            visible.add((row, col))
            h = forest[row][col]

    h = forest[row][cols - 1]

    for col in reversed(range(1, cols - 1)):
        if h < forest[row][col]:
            visible.add((row, col))
            h = forest[row][col]

for col in range(1, cols - 1):
    h = forest[0][col]

    for row in range(1, rows - 1):
        if h < forest[row][col]:
            visible.add((row, col))
            h = forest[row][col]

    h = forest[rows - 1][col]

    for row in reversed(range(1, rows - 1)):
        if h < forest[row][col]:
            visible.add((row, col))
            h = forest[row][col]


part_1 += len(visible)

print(part_1)

part_2 = 0

for row in range(rows):
    for col in range(cols):
        scenic = [0] * 4

        for c in range(col + 1, cols):
            if forest[row][c] < forest[row][col]:
                scenic[0] += 1
            else:
                scenic[0] += int(c < cols)
                break

        for c in range(col - 1, -1, -1):
            if forest[row][c] < forest[row][col]:
                scenic[1] += 1
            else:
                scenic[1] += int(c >= 0)
                break

        for r in range(row + 1, rows):
            if forest[r][col] < forest[row][col]:
                scenic[2] += 1
            else:
                scenic[2] += int(r < rows)
                break

        for r in range(row - 1, -1, -1):
            if forest[r][col] < forest[row][col]:
                scenic[3] += 1
            else:
                scenic[3] += int(r >= 0)
                break

        part_2 = max(part_2, scenic[0] * scenic[1] * scenic[2] * scenic[3])

        print(row, col, scenic)

print(part_2)
