import operator
import pathlib

data = pathlib.Path("../../data/2015/02.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

presents = [[int(n) for n in line.split("x")] for line in lines]


part_1 = 0
part_2 = 0

for l, w, h in presents:
    part_1 += 2 * (l * w + w * h + l * h) + operator.mul(*sorted([l, w, h])[:2])
    part_2 += 2 * operator.add(*sorted([l, w, h])[:2]) + l * w * h

print(part_1)
print(part_2)
