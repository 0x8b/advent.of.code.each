import json
import re


def ints(line):
    return list(int(s) for s in re.findall(r"(?:\-|\+)?\d+", line))


def digits(line):
    return list(int(s) for s in re.findall(r"\d", line))


def matrix(data, *, separator=",", try_parse=False):
    if isinstance(data, str):
        data = data.split("\n")

    assert isinstance(data, list)

    if len(data) and not all(isinstance(row, list) for row in data):
        data = [(row.split(separator) if separator else list(row)) for row in data]

    assert (
        len(data)
        and all(isinstance(row, list) for row in data)
        and len(set(len(row) for row in data)) == 1
    )

    if try_parse:
        for y in range(len(data)):
            for x in range(len(data[0])):
                try:
                    data[y][x] = json.loads(data[y][x])
                except Exception:
                    pass

    return data


def print_matrix(matrix, separator=""):
    print("\n".join(separator.join(str(c) for c in row) for row in matrix))
