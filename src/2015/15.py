import pathlib
from functools import reduce
from itertools import batched, product

from utils import *

data = pathlib.Path("../../data/2015/15.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

ingredients = []

for line in lines:
    ingredient, *props = line.replace(":", "").replace(",", "").split(" ")

    props = dict((prop, int(value)) for prop, value in batched(props, 2))

    ingredients.append(props)

max_score = 0
max_score_with_500_calories = 0

for combo in product(range(101), repeat=len(ingredients)):
    if sum(combo) != 100:
        continue

    scores = [
        sum(ingredients[i][prop] * combo[i] for i in range(len(ingredients)))
        for prop in ["capacity", "durability", "flavor", "texture"]
    ]

    score = reduce(
        lambda total, score: total * score, [max(0, score) for score in scores], 1
    )

    max_score = max(max_score, score)

    if (
        sum(ingredients[i]["calories"] * combo[i] for i in range(len(ingredients)))
        == 500
    ):
        max_score_with_500_calories = max(max_score_with_500_calories, score)

part_1 = max_score

print(part_1)

part_2 = max_score_with_500_calories

print(part_2)
