import pathlib
import string
from copy import deepcopy

from utils import *

data = pathlib.Path("../../data/2018/07.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")


edges = {}

for line in lines:
    a, b = line[5], line[36]

    if b not in edges:
        edges[b] = {a}
    else:
        edges[b].add(a)

    if a not in edges:
        edges[a] = set()

edges_copy = deepcopy(edges)

part_1 = ""

while edges:
    ready = sorted([key for key, value in edges.items() if len(value) == 0])[0]

    part_1 += ready

    for key, value in edges.items():
        value.difference_update(set(ready))

    del edges[ready]

print(part_1)

seconds = dict(
    (letter, 60 + ord(letter) - ord("A") + 1) for letter in string.ascii_uppercase
)

workers = [0] * 5
workers_letters = [None] * 5

edges = edges_copy

part_2 = 0

picked = set()

while edges:
    idle_worker_indices = [i for i, value in enumerate(workers) if value == 0]
    available_tasks = sorted(
        [
            task
            for task, tasks in edges.items()
            if len(tasks) == 0 and task not in picked
        ]
    )

    for worker_index, task in zip(idle_worker_indices, available_tasks):
        workers[worker_index] += seconds[task]
        workers_letters[worker_index] = task
        picked.add(task)

    workers = [max(0, workers[i] - 1) for i in range(len(workers))]

    for worker_index, remaining_seconds in enumerate(workers):
        if remaining_seconds == 0 and (letter := workers_letters[worker_index]):
            workers_letters[worker_index] = None

            for key, value in edges.items():
                edges[key].difference_update({letter})

            del edges[letter]

    part_2 += 1

print(part_2)
