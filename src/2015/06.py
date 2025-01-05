import pathlib
import re
from collections import defaultdict

data = pathlib.Path("../../data/2015/06.txt").read_text(encoding="utf-8")

grid = defaultdict(bool)
brightness = defaultdict(int)

for match in re.finditer(
    r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)", data, re.MULTILINE
):
    action, start_x, start_y, end_x, end_y = match.groups()

    for x in range(int(start_x), int(end_x) + 1):
        for y in range(int(start_y), int(end_y) + 1):
            match action:
                case "turn on":
                    grid[x, y] = True
                    brightness[x, y] += 1
                case "turn off":
                    grid[x, y] = False
                    brightness[x, y] = max(0, brightness[x, y] - 1)
                case "toggle":
                    grid[x, y] = not grid[x, y]
                    brightness[x, y] += 2

part_1 = sum(grid.values())
part_2 = sum(brightness.values())

print(part_1)
print(part_2)
