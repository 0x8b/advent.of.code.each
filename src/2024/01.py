import pathlib
from collections import Counter

data = pathlib.Path("../../data/2024/01.txt").read_text(encoding="utf-8")

lines = data.strip().split("\n")

pairs = [line.split() for line in lines]

[left, right] = list(zip(*pairs))

left = list(sorted(left))
right = list(sorted(right))

print(sum(abs(int(l) - int(r)) for l, r in zip(left, right)))

counter = Counter(right)

print(sum([(counter[n] * int(n) if n in counter else 0) for n in left]))
