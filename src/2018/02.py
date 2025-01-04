import pathlib
from collections import Counter
from itertools import combinations

from utils import *

data = pathlib.Path("../../data/2018/02.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

twos, threes = 0, 0

for line in lines:
    c = Counter(line).values()

    twos += int(2 in c)
    threes += int(3 in c)

part_1 = twos * threes

print(part_1)

for id_1, id_2 in combinations(lines, 2):
    if [ch_1 != ch_2 for ch_1, ch_2 in zip(id_1, id_2)].count(True) == 1:
        part_2 = "".join(ch_1 for ch_1, ch_2 in zip(id_1, id_2) if ch_1 == ch_2)
        print(part_2)
        break
