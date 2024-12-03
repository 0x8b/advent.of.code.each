import functools
import pathlib
import re

data = pathlib.Path("../../data/2024/03.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

memory = "".join(lines)


def get_answer(memory, pattern):
    enabled = True
    answer = 0

    for instr in re.findall(pattern, memory):
        match instr:
            case _ if instr.startswith("don't"):
                enabled = False
            case _ if instr.startswith("do"):
                enabled = True
            case _ if instr.startswith("mul"):
                if enabled:
                    answer += functools.reduce(
                        lambda product, m: product * m,
                        [int(s) for s in re.findall(r"\d+", instr)],
                        1,
                    )
            case _:
                raise ValueError(f"unsupported instruction {instr}")

    return answer


part_1 = get_answer(memory, r"mul\(\d{1,3},\d{1,3}\)")
part_2 = get_answer(memory, r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)")

print(part_1)
print(part_2)
