import pathlib
import re

data = pathlib.Path("../../data/2015/05.txt").read_text(encoding="utf-8")
strings = data.strip().split("\n")

part_1 = 0
part_2 = 0

for string in strings:
    if (
        len(list(filter(lambda ch: ch in "aeiou", string))) >= 3
        and any(a == b for a, b in zip(string, string[1:]))
        and "ab" not in string
        and "cd" not in string
        and "pq" not in string
        and "xy" not in string
    ):
        part_1 += 1

    if any(
        a == c and b != c for a, b, c in zip(string, string[1:], string[2:])
    ) and re.findall(r"(.)(.).*(\1\2)", string):
        part_2 += 1

print(part_1)
print(part_2)
