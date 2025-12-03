import pathlib

from utils import *

data = pathlib.Path("../../data/2025/03.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")


def get_largest_joltage(bank, size):
    available, stash = bank[: -size + 1], bank[-size + 1 :] + [0]
    joltage = []

    for _ in range(size):
        index = available.index(max(*available, 0))

        joltage.append(available[index])
        available = available[index + 1 :] + [stash.pop(0)]

    return int("".join(str(d) for d in joltage))


part_1 = 0
part_2 = 0

for line in lines:
    bank = [int(d) for d in line]

    part_1 += get_largest_joltage(bank, 2)
    part_2 += get_largest_joltage(bank, 12)

print(part_1)
print(part_2)
