import pathlib

from utils import *

data = pathlib.Path("../../data/2023/05.txt").read_text(encoding="utf-8")
seeds, *maps = data.strip().split("\n\n")

seeds = ints(seeds)

MAPS = []

for map in maps:
    categories, *lines = map.strip().split("\n")

    source_category, _, destination_category = categories.split(" ")[0].split("-")

    MAPS.append((source_category, destination_category, [ints(line) for line in lines]))
