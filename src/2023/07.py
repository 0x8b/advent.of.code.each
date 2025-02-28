import pathlib
from collections import Counter

from utils import *

data = pathlib.Path("../../data/2023/07.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

data = []

for line in lines:
    hand, bid = line.split()

    c = list(sorted(Counter(hand).values()))

    if c == [5]:
        type_of_hand = 6
    elif c == [1, 4]:
        type_of_hand = 5
    elif c == [2, 3]:
        type_of_hand = 4
    elif c == [1, 1, 3]:
        type_of_hand = 3
    elif c == [1, 2, 2]:
        type_of_hand = 2
    elif c == [1, 1, 1, 2]:
        type_of_hand = 1
    elif c == [1, 1, 1, 1, 1]:
        type_of_hand = 0
    else:
        type_of_hand = None

    order = dict(zip("23456789TJQKA", range(20)))

    rank = tuple(order[card] for card in hand)

    data.append([hand, bid, (type_of_hand, *rank)])

data = sorted(data, key=lambda d: d[2])

print(data)

part_1 = 0

for i, d in enumerate(data, 1):
    part_1 += i * int(d[1])

print(part_1)