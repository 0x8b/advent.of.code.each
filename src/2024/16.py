import pathlib

from utils import *

data = pathlib.Path("../../data/2024/16.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

maze = matrix(lines, separator="")

for row in range(len(maze)):
    for col in range(len(maze[0])):
        if maze[row][col] == "S":
            reindeer_row = row
            reindeer_col = col

        elif maze[row][col] == "E":
            end_tile_row = row
            end_tile_col = col
