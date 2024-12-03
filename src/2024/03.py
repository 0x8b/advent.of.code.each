import functools
import pathlib
import re

data = pathlib.Path("../../data/2024/03.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

memory = "".join(lines)

part_1 = sum(
    [
        int(pair[0]) * int(pair[1])
        for pair in [
            re.findall(r"\d+", mul)
            for mul in re.findall(r"mul\(\d{1,3},\d{1,3}\)", memory)
        ]
    ]
)

print(part_1)


enabled = True
part_2 = 0

for instr in re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", memory):
    match instr:
        case _ if instr.startswith("don't"):
            enabled = False
        case _ if instr.startswith("do"):
            enabled = True
        case _ if instr.startswith("mul"):
            if enabled:
                part_2 += functools.reduce(
                    lambda product, m: product * m,
                    [int(s) for s in re.findall(r"\d+", instr)],
                    1,
                )
        case _:
            raise ValueError(f"nieobsługiwana instrukcja {instr}")

print(part_2)
