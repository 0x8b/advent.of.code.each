import pathlib

from utils import *

data = pathlib.Path("../../data/2016/18.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")


for rows in [40, 400_000]:
    room = list(lines[0])

    answer = room.count(".")

    for i in range(rows - 1):
        room = [
            "^" if f"{left}{center}{right}" in ["^^.", ".^^", "^..", "..^"] else "."
            for left, center, right in zip(["."] + room, room, room[1:] + ["."])
        ]

        answer += room.count(".")

    print(answer)  # part_1, part_2
