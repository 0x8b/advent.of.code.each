import operator
import pathlib
import re

data = pathlib.Path("../../data/2024/03.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

memory = "".join(lines)


def get_answer(memory, pattern):
    enabled = True
    answer = 0

    for instr in re.finditer(pattern, memory):
        match [m for m in instr.groups() if m is not None]:
            case ["do"]:
                enabled = True
            case ["don't"]:
                enabled = False
            case ["mul", a, b]:
                if enabled:
                    answer += int(a) * int(b)
            case _:
                raise ValueError(f"unsupported instruction {instr}")

    return answer


part_1 = get_answer(memory, r"(mul)\((\d{1,3}),(\d{1,3})\)")
part_2 = get_answer(memory, r"(mul)\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don't)\(\)")

print(part_1)
print(part_2)
