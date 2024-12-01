import pathlib

data = pathlib.Path("../../data/2024/18.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

