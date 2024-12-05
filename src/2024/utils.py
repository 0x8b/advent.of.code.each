import re


def ints(line):
    return list(int(s) for s in re.findall(r"\d+", line))
