import pathlib

from utils import *

data = pathlib.Path("../../data/2024/22.txt").read_text(encoding="utf-8")

secret_numbers = ints(data)

part_1 = 0

for secret_number in secret_numbers:
    for i in range(2000):
        secret_number = (secret_number ^ (secret_number * 64)) % 16777216
        secret_number = ((secret_number // 32) ^ secret_number) % 16777216
        secret_number = ((secret_number * 2048) ^ secret_number) % 16777216

    part_1 += secret_number

print(part_1)
