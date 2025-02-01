import pathlib
from collections import Counter
from itertools import batched
from operator import itemgetter

from utils import *

data = pathlib.Path("../../data/2019/08.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

password = lines[0]

wide, tall = 25, 6

layers = list(batched(list(password), wide * tall))

counters = [Counter(layer) for layer in layers]

layer_with_fewers_0 = min(counters, key=itemgetter("0"))

part_1 = layer_with_fewers_0["1"] * layer_with_fewers_0["2"]

print(part_1)

pixels = ["".join(stack).lstrip("2")[0] for stack in zip(*layers)]

for row in range(tall):
    for col in range(wide):
        print("█" if pixels[row * wide + col] == "1" else " ", end="")  # part_2

    print()
