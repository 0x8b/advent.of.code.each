import pathlib

from utils import *

data = pathlib.Path("../../data/2016/05.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

password = lines[0]

print(password)
