import itertools
import pathlib

from utils import *

data = pathlib.Path("../../data/2018/01.txt").read_text(encoding="utf-8")

frequencies = ints(data)

print(sum(frequencies))  # part_1

seen_frequencies = {0}
frequency = 0

for f in itertools.cycle(frequencies):
    frequency += f

    if frequency in seen_frequencies:
        print(frequency)  # part_2
        break

    seen_frequencies.add(frequency)
