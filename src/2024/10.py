import pathlib

data = pathlib.Path("../../data/2024/10.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

print(lines)