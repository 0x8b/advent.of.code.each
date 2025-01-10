import pathlib

from utils import *

data = pathlib.Path("../../data/2017/05.txt").read_text(encoding="utf-8")
offsets = ints(data)


index = 0
steps = 0

while 0 <= index < len(offsets):
    value = offsets[index]

    offsets[index] += 1
    index += value

    steps += 1

part_1 = steps

print(part_1)


offsets = ints(data)
index = 0
steps = 0

while 0 <= index < len(offsets):
    value = offsets[index]

    offsets[index] += -1 if value >= 3 else 1
    index += value

    steps += 1

part_2 = steps

print(part_2)
