import pathlib

data = pathlib.Path("../../data/2017/01.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

digits = lines[0]


part_1 = sum(
    int(pair[0]) for pair in zip(digits, digits[1:]) if pair[0] == pair[1]
) + int(digits[-1])

print(part_1)

part_2 = sum(
    int(pair[0])
    for pair in zip(digits, digits[len(digits) // 2 :] + digits[: len(digits) // 2])
    if pair[0] == pair[1]
)

print(part_2)
