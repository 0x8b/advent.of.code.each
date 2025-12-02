import pathlib

from utils import *

data = pathlib.Path("../../data/2025/02.txt").read_text(encoding="utf-8").strip()

data = matrix(data, row_separator=",", separator="-", try_parse=True)

part_1 = 0
part_2 = 0

for begin, end in data:
    for id in range(begin, end + 1):
        seq = str(id)

        if seq[: len(seq) // 2] == seq[len(seq) // 2 :]:
            part_1 += id

        for divisor in range(1, len(seq)):
            if len(seq) % divisor == 0:
                if seq == seq[:divisor] * (len(seq) // divisor):
                    part_2 += id
                    break

print(part_1)
print(part_2)
