import pathlib

from utils import *

data = pathlib.Path("../../data/2025/04.txt").read_text(encoding="utf-8")

data = matrix(data, separator="")

part_1 = 0

for y in range(0, len(data)):
    for x in range(0, len(data[0])):
        count = 0

        if data[y][x] != "@":
            continue

        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue

                xx = x + dx
                yy = y + dy

                if 0 <= yy < len(data) and 0 <= xx < len(data[0]):
                    count += data[yy][xx] == "@"

        part_1 += count < 4

print(part_1)

part_2 = 0

while True:
    deleted = False

    for y in range(0, len(data)):
        for x in range(0, len(data[0])):
            count = 0

            if data[y][x] != "@":
                continue

            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue

                    xx = x + dx
                    yy = y + dy

                    if 0 <= yy < len(data) and 0 <= xx < len(data[0]):
                        count += data[yy][xx] == "@"

            if count < 4:
                deleted = True
                data[y][x] = "x"
                part_2 += 1

    if deleted == False:
        break

print(part_2)
