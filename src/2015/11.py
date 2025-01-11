import pathlib
import re
import string

from utils import *

data = pathlib.Path("../../data/2015/11.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

password = lines[0]

triples = list(
    "".join(t)
    for t in zip(
        string.ascii_lowercase, string.ascii_lowercase[1:], string.ascii_lowercase[2:]
    )
)

pairs = list(a + a for a in string.ascii_lowercase)


def successor(s):
    strip_zs = s.rstrip("z")

    if strip_zs:
        return (
            strip_zs[:-1] + chr(ord(strip_zs[-1]) + 1) + "a" * (len(s) - len(strip_zs))
        )
    else:
        return "a" * (len(s) + 1)


def next_valid_password(password):
    while True:
        password = successor(password)

        if (
            "i" not in password
            and "l" not in password
            and "o" not in password
            and any(triple in password for triple in triples)
            and re.search(r"(.)\1.*?(.)\2", password)
        ):
            return password


part_1 = next_valid_password(password)
print(part_1)

part_2 = next_valid_password(part_1)
print(part_2)
