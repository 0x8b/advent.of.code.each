import pathlib
from collections import Counter


data = pathlib.Path("../../data/2019/04.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

start, stop = lines[0].split("-")

part_1 = 0
part_2 = 0

for password in range(int(start), int(stop) + 1):
    if list(str(password)) == list(sorted(str(password))) and any(
        t[0] == t[1] for t in zip(str(password), str(password)[1:])
    ):
        part_1 += 1

        if 2 in Counter(str(password)).values():
            part_2 += 1

print(part_1)
print(part_2)
