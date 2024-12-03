import operator
import pathlib
import re

data = pathlib.Path("../../data/2024/03.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

memory = "".join(lines)


def get_answer(memory, pattern):
    enabled = True
    answer = 0

    for instr in re.findall(pattern, memory):
        if instr.startswith("don't"):
            enabled = False
        elif instr.startswith("do"):
            enabled = True
        elif instr.startswith("mul"):
            if enabled:
                answer += operator.mul(*[int(s) for s in re.findall(r"\d+", instr)])
        else:
            raise ValueError(f"unsupported instruction {instr}")

    return answer


part_1 = get_answer(memory, r"mul\(\d{1,3},\d{1,3}\)")
part_2 = get_answer(memory, r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)")

print(part_1)
print(part_2)
