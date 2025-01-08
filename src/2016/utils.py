import re


def ints(line):
    return list(int(s) for s in re.findall(r"(?:\-|\+)?\d+", line))


def transpose(matrix):
    assert (
        len(matrix)
        and isinstance(matrix, list)
        and all(isinstance(row, list) for row in matrix)
        and len(set(len(row) for row in matrix)) == 1
    )

    return [list(row) for row in zip(*matrix)]


def print_matrix(matrix, separator=""):
    print("\n".join(separator.join(str(c) for c in row) for row in matrix))
