import pathlib

import utils

data = pathlib.Path("../../data/2024/14.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

print(lines)
