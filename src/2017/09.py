import pathlib

from utils import *

data = pathlib.Path("../../data/2017/09.txt").read_text(encoding="utf-8")
stream = data.strip()


def calculate_total_score_for_all_groups(stream):
    score = 0
    stack = 0
    state = "char"
    garbage_count = 0

    for ch in stream:
        match state:
            case "char":
                if ch == "{":
                    stack += 1
                elif ch == "}":
                    score += stack
                    stack -= 1
                elif ch == "!":
                    state = "skip_char"
                elif ch == "<":
                    state = "garbage"
                else:
                    pass

            case "skip_char":
                state = "char"

            case "garbage":
                if ch == ">":
                    state = "char"
                elif ch == "!":
                    state = "skip_garbage"
                else:
                    garbage_count += 1

            case "skip_garbage":
                state = "garbage"

    return score, garbage_count


part_1, part_2 = calculate_total_score_for_all_groups(stream)

print(part_1)
print(part_2)
