import json
import pathlib

from utils import *

data = pathlib.Path("../../data/2015/12.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

json_structure = lines[0]

part_1 = sum(ints(json_structure))

print(part_1)


def replace_red_dicts_with_zero(obj):
    if isinstance(obj, dict) and "red" in obj.values():
        return 0

    if isinstance(obj, list):
        return [replace_red_dicts_with_zero(value) for value in obj]
    elif isinstance(obj, dict):
        for key in obj:
            obj[key] = replace_red_dicts_with_zero(obj[key])

    return obj


part_2 = sum(ints(json.dumps(replace_red_dicts_with_zero(json.loads(json_structure)))))

print(part_2)
