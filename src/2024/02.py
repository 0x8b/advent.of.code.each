import pathlib

data = pathlib.Path("../../data/2024/02.txt").read_text(encoding="utf-8")
reports = [list([int(n) for n in line.split()]) for line in data.strip().split("\n")]


def is_increasing(seq, index_to_remove=None):
    cloned_seq = [n for n in seq]

    if index_to_remove is not None:
        cloned_seq.pop(index_to_remove)

    return cloned_seq == list(sorted(cloned_seq))


def is_decreasing(seq, index_to_remove=None):
    cloned_seq = [n for n in seq]

    if index_to_remove is not None:
        cloned_seq.pop(index_to_remove)

    return cloned_seq == list(reversed(sorted(cloned_seq)))


def is_difference_within_range(seq, minimum, maximum, index_to_remove=None):
    cloned_seq = [n for n in seq]

    if index_to_remove is not None:
        cloned_seq.pop(index_to_remove)

    for i in range(len(cloned_seq) - 1):
        if not (minimum <= abs(cloned_seq[i] - cloned_seq[i + 1]) <= maximum):
            return False

    return is_decreasing(cloned_seq) or is_increasing(cloned_seq)


part_1 = 0
part_2 = 0

for report in reports:
    if is_increasing(report) or is_decreasing(report):
        if is_difference_within_range(report, 1, 3):
            part_1 += 1

    if (
        is_increasing(report)
        or is_decreasing(report)
        or any(is_increasing(report, i) for i in range(len(report)))
        or any(is_decreasing(report, i) for i in range(len(report)))
    ):
        if is_difference_within_range(report, 1, 3) or any(
            is_difference_within_range(report, 1, 3, i) for i in range(len(report))
        ):
            part_2 += 1

print(part_1)
print(part_2)
