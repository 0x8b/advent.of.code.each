import pathlib

from tqdm import tqdm
from utils import *

data = pathlib.Path("../../data/2017/15.txt").read_text(encoding="utf-8")

A, B = ints(data)

a, b = A, B

part_1 = 0

mask = 2**16 - 1

for _ in tqdm(range(40_000_000)):
    part_1 += int(a & mask == b & mask)

    a = (a * 16807) % 2147483647
    b = (b * 48271) % 2147483647

print(part_1)


def gen(n, d, m):
    while True:
        if n % d == 0:
            yield n

        n = (n * m) % 2147483647


part_2 = 0

ga = gen(A, 4, 16807)
gb = gen(B, 8, 48271)

for _ in tqdm(range(5_000_000)):
    a = next(ga)
    b = next(gb)

    part_2 += int(a & mask == b & mask)

print(part_2)
