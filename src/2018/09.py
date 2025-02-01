import pathlib
from collections import defaultdict
from dataclasses import dataclass
from itertools import cycle
from typing import Optional, Self

from utils import *

data = pathlib.Path("../../data/2018/09.txt").read_text(encoding="utf-8")

players, last_marble_worth = ints(data)


@dataclass
class Node:
    def __init__(
        self, value: int, prev: Optional[Self] = None, next: Optional[Self] = None
    ):
        self.value = value
        self.prev = prev
        self.next = next


for last_marble in [last_marble_worth, 100 * last_marble_worth]:
    circle = Node(0)
    circle.next = circle
    circle.prev = circle

    scores = defaultdict(int)

    current_marble = circle

    for player, marble in zip(cycle(range(1, players + 1)), range(1, last_marble + 1)):
        if marble % 23 == 0:
            for _ in range(7):
                current_marble = current_marble.prev

            scores[player] += current_marble.value + marble

            prev_marble, next_marble = current_marble.prev, current_marble.next

            current_marble.prev.next, current_marble.next.prev = (
                next_marble,
                prev_marble,
            )

            current_marble = next_marble
        else:
            new_node = Node(marble, current_marble.next, current_marble.next.next)

            current_marble.next.next.prev = new_node
            current_marble.next.next = new_node

            current_marble = new_node

    answer = max(scores.values())  # part_1, part_2

    print(answer)
