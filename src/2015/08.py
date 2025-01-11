import pathlib

from utils import *

data = pathlib.Path("../../data/2015/08.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

part_1 = 0
part_2 = 0

for line in lines:
    part_1 += len(line) - int(eval(f"len({line})"))
    part_2 += len(line) + 2 + line.count('"') + line.count("\\") - len(line)

print(part_1)
print(part_2)
