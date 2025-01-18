import pathlib

from utils import *

data = pathlib.Path("../../data/2017/06.txt").read_text(encoding="utf-8")
memory_banks = ints(data)

seen = set()

first_repeated = None

redistributions_counter = 0

while True:
    most_blocks = max(memory_banks)

    most_blocks_index = memory_banks.index(most_blocks)

    memory_banks[most_blocks_index] = 0

    for i in range(most_blocks):
        memory_banks[(most_blocks_index + 1 + i) % len(memory_banks)] += 1

    redistributions_counter += 1

    if first_repeated is None:
        if tuple(memory_banks) in seen:
            part_1 = redistributions_counter

            print(part_1)

            first_repeated = tuple(memory_banks)
            redistributions_counter = 0

        seen.add(tuple(memory_banks))

    else:
        if tuple(memory_banks) == first_repeated:
            part_2 = redistributions_counter

            print(part_2)

            break
