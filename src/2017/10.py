import pathlib
from functools import reduce
from itertools import batched

from utils import *

data = pathlib.Path("../../data/2017/10.txt").read_text(encoding="utf-8")

lenghts = ints(data)

numbers = list(range(256))

skip = 0
current_position = 0

for length in lenghts:
    indices = [(current_position + i) % len(numbers) for i in range(length)]

    values = list(reversed([numbers[i] for i in indices]))

    for i, v in enumerate(values):
        numbers[indices[i]] = v

    current_position = (current_position + length + skip) % len(numbers)
    skip += 1

part_1 = numbers[0] * numbers[1]

print(part_1)


def knot_hash(string):
    lenghts = [ord(s) for s in string] + [17, 31, 73, 47, 23]
    sparse_hash = list(range(256))
    skip = 0
    current_position = 0

    for _ in range(64):
        for length in lenghts:
            indices = [(current_position + i) % len(sparse_hash) for i in range(length)]

            values = list(reversed([sparse_hash[i] for i in indices]))

            for i, v in enumerate(values):
                sparse_hash[indices[i]] = v

            current_position = (current_position + length + skip) % len(sparse_hash)
            skip += 1

    dense_hash = "".join(
        [
            hex(reduce(lambda a, b: a ^ b, seq))[2:].zfill(2)
            for seq in batched(numbers, 16)
        ]
    )

    return dense_hash


part_2 = knot_hash(data.strip())

print(part_2)
