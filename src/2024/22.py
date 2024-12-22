import itertools
import pathlib

from utils import *

data = pathlib.Path("../../data/2024/22.txt").read_text(encoding="utf-8")

secret_numbers = ints(data)

part_1 = 0

all_changes = []

for secret_number in secret_numbers:
    sequence = []
    prices = [secret_number % 10]
    changes = {}

    for i in range(2000):
        secret_number = (secret_number ^ (secret_number * 64)) % 16777216
        secret_number = ((secret_number // 32) ^ secret_number) % 16777216
        secret_number = ((secret_number * 2048) ^ secret_number) % 16777216

        prices.append(secret_number % 10)

        sequence.append(prices[-1] - prices[-2])

        sequence = sequence[-4:]

        if len(sequence) == 4:
            if tuple(sequence) not in changes:
                changes[tuple(sequence)] = prices[-1]
            else:
                pass

    all_changes.append(changes)

    part_1 += secret_number

print(part_1)

sequences = set()
for changes in all_changes:
    sequences.update(set(changes.keys()))

part_2 = 0

for sequence in sequences:
    score = 0

    for changes in all_changes:
        if sequence in changes:
            score += changes[sequence]

    part_2 = max(score, part_2)

print(part_2)
