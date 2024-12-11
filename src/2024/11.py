import pathlib
from functools import cache

from utils import *

data = pathlib.Path("../../data/2024/11.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

stones = ints(lines[0])


@cache
def count_stones(stone, blink):
    if blink == 0:
        return 1

    match stone:
        case 0:
            count = count_stones(1, blink - 1)
        case value if len(str(value)) % 2 == 0:
            value = str(value)
            mid = len(value) // 2

            count = count_stones(int(value[:mid]), blink - 1) + count_stones(
                int(value[mid:]), blink - 1
            )
        case value:
            count = count_stones(value * 2024, blink - 1)

    return count


part_1 = 0
part_2 = 0

for stone in stones:
    part_1 += count_stones(stone, 25)
    part_2 += count_stones(stone, 75)

print(part_1)
print(part_2)
