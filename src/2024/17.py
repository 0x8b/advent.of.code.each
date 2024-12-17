import pathlib

from utils import *

data = pathlib.Path("../../data/2024/17.txt").read_text(encoding="utf-8")

rega, regb, regc, *program = ints(data)

print(rega, regb, regc, program)
