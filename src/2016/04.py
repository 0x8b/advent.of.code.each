import pathlib
import re
from collections import Counter

from utils import *

data = pathlib.Path("../../data/2016/04.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")


def rotate_chr(ch, rot):
    return chr(ord("a") + (ord(ch) - ord("a") + rot) % 26) if ch != "-" else ch


part_1 = 0
part_2 = 0

for line in lines:
    match = re.match(r"(.*)-(\d+)\[(.*)\]", line)

    encrypted_name, id, checksum = match.groups()

    c = Counter(sorted(list(encrypted_name.replace("-", ""))))

    if "".join(ch for ch, _ in c.most_common(len(checksum))) == checksum:
        part_1 += int(id)

    rotated = "".join(rotate_chr(ch, int(id)) for ch in encrypted_name)

    if "north" in rotated:
        part_2 = id

print(part_1)
