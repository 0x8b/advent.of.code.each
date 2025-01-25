import pathlib

from utils import *

data = pathlib.Path("../../data/2017/16.txt").read_text(encoding="utf-8")

moves = data.strip().split(",")

program = list("abcdefghijklmnop")

seen = set()

seen.add("abcdefghijklmnop")

history = []

for i in range(1000000000):
    for move in moves:
        if move[0] == "s":
            spin = int(move[1:])
            program = program[-spin:] + program[:-spin]

        elif move[0] == "x":
            a, b = move[1:].split("/")
            a, b = int(a), int(b)

            program[a], program[b] = program[b], program[a]

        elif move[0] == "p":
            a, b = move[1:].split("/")

            ai = program.index(a)
            bi = program.index(b)

            program[ai], program[bi] = program[bi], program[ai]

    seq = "".join(program)

    history.append(seq)

    if seq in seen:
        break
    else:
        seen.add(seq)


part_1 = history[0]

print(part_1)


part_2 = history[(1000000000 - 1) % len(history)]

print(part_2)
