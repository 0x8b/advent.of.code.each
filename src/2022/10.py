import pathlib

from utils import *

data = pathlib.Path("../../data/2022/10.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

x = 1

for line in lines:
    match line.strip().split():
        case ["noop"]:
            ...

        case ["addx", value]:
            ...
