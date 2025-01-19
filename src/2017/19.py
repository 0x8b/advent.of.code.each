import pathlib

from utils import *

data = pathlib.Path("../../data/2017/19.txt").read_text(encoding="utf-8")

grid = matrix(data, separator="", prevent_strip=True)

steps = 0

row, col = 0, grid[0].index("|")
previous_row, previous_col = -1, col

part_1 = ""

while True:

    if grid[row][col].isupper():
        part_1 += grid[row][col]

    drow, dcol = row - previous_row, col - previous_col

    if grid[row][col] == " ":
        break

    if grid[row][col] == "+":
        previous_row = row
        previous_col = col

        for r, c in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            if (r, c) != (drow, dcol) and (r, c) != (-drow, -dcol):
                if grid[row + r][col + c] != " ":
                    row = row + r
                    col = col + c
                    break
    else:
        previous_row = row
        previous_col = col

        row = row + drow
        col = col + dcol

    steps += 1

print(part_1)

part_2 = steps

print(part_2)
