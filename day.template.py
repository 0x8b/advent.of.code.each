import pathlib

from utils import *

data = pathlib.Path("../../data/YYYY/DD.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

print(lines)
