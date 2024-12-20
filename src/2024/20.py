import pathlib

from utils import *

data = pathlib.Path("../../data/2024/20.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

racetrack = matrix(lines, separator="")

rows, cols = len(racetrack), len(racetrack[0])

for row in rows:
    for col in cols:
        if racetrack[row][col] == "S":
            start_row, start_col = row, col
            racetrack[row][col] = "."

        if racetrack[row][col] == "E":
            end_row, end_col = row, col
            racetrack[row][col] = "."

print(racetrack)
