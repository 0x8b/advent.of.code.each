import pathlib

import networkx

data = pathlib.Path("../../data/2015/07.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")


PART_2 = False

edges = []

signals = {}

for line in lines:
    match line.split(" "):
        case [in_1, "RSHIFT", in_2, "->", out]:
            if in_1.isalpha():
                edges.append((in_1, out))

            if in_2.isalpha():
                edges.append((in_2, out))

            signals[out] = ["RSHIFT", in_1, in_2, out]

        case [in_1, "LSHIFT", in_2, "->", out]:
            if in_1.isalpha():
                edges.append((in_1, out))

            if in_2.isalpha():
                edges.append((in_2, out))

            signals[out] = ["LSHIFT", in_1, in_2, out]

        case [in_1, "OR", in_2, "->", out]:
            if in_1.isalpha():
                edges.append((in_1, out))

            if in_2.isalpha():
                edges.append((in_2, out))

            signals[out] = ["OR", in_1, in_2, out]

        case [in_1, "AND", in_2, "->", out]:
            if in_1.isalpha():
                edges.append((in_1, out))

            if in_2.isalpha():
                edges.append((in_2, out))

            signals[out] = ["AND", in_1, in_2, out]

        case ["NOT", in_1, "->", out]:
            if in_1.isalpha():
                edges.append((in_1, out))

            signals[out] = ["NOT", in_1, out]

        case [in_1, "->", out]:
            if in_1.isalpha():
                edges.append((in_1, out))

            signals[out] = int(in_1) if in_1.isdigit() else [in_1, out]

        case other:
            raise ValueError(other)


topological_sorted = list(networkx.dag.topological_sort(networkx.DiGraph(edges)))


def get_signal(input):
    if input.isdigit():
        return int(input)
    else:
        return int(signals[input])


if PART_2:
    signals["b"] = 46065

for out in topological_sorted:
    match signals.get(out):
        case ["AND", a, b, c]:
            signals[c] = get_signal(a) & get_signal(b)

        case ["OR", a, b, c]:
            signals[c] = get_signal(a) | get_signal(b)

        case ["LSHIFT", a, b, c]:
            signals[c] = (get_signal(a) << get_signal(b)) & (2**16 - 1)

        case ["RSHIFT", a, b, c]:
            signals[c] = (get_signal(a) >> get_signal(b)) & (2**16 - 1)

        case ["NOT", a, b]:
            signals[b] = get_signal(a) ^ (2**16 - 1)

        case [a, b]:
            signals[b] = get_signal(a)

        case integer if isinstance(integer, int):
            ...


print(signals["a"])  # part_1, part_2
