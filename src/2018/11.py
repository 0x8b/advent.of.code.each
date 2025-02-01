import pathlib

from utils import *

data = pathlib.Path("../../data/2018/11.txt").read_text(encoding="utf-8")

grid_serial_number = int(data.strip())


xs, ys = 300, 300

grid = [[0] * xs for _ in range(ys)]

for x in range(1, xs + 1):
    for y in range(1, ys + 1):
        rack_id = x + 10

        grid[x - 1][y - 1] = (
            ((rack_id * y + grid_serial_number) * rack_id % 1000) // 100
        ) - 5


largest = None
largest_x, largest_y = 1, 1

for x in range(1, xs - 1):
    for y in range(1, ys - 1):
        maybe_largest = 0

        for dx in range(0, 3):
            for dy in range(0, 3):
                maybe_largest += grid[x - 1 + dx][y - 1 + dy]

        if largest is None:
            largest = maybe_largest

        elif maybe_largest > largest:
            largest = maybe_largest

            largest_x = x
            largest_y = y

part_1 = f"{largest_x},{largest_y}"

print(part_1)


largest = None
largest_x, largest_y, largest_size = 1, 1, 2

for size in range(2, 20):
    for x in range(1, xs + 1 - size + 1):
        for y in range(1, ys + 1 - size + 1):
            maybe_largest = 0

            for dx in range(0, size):
                for dy in range(0, size):
                    maybe_largest += grid[x - 1 + dx][y - 1 + dy]

            if largest is None:
                largest = maybe_largest

            elif maybe_largest > largest:
                largest = maybe_largest

                largest_x = x
                largest_y = y
                largest_size = size

part_2 = f"{largest_x},{largest_y},{largest_size}"

print(part_2)
