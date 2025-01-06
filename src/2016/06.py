import pathlib
from collections import Counter

from utils import *

data = pathlib.Path("../../data/2016/06.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

columns = transpose([list(line) for line in lines])

counters = [Counter(column).most_common() for column in columns]

part_1 = "".join([c[0][0] for c in counters])
part_2 = "".join([c[-1][0] for c in counters])

print(part_1)
print(part_2)
