import pathlib
from collections import deque

from utils import *

data = pathlib.Path("../../data/2018/08.txt").read_text(encoding="utf-8")


nslf = deque(ints(data))


def build_tree(nslf):
    quantity_of_child_nodes = nslf.popleft()
    quantify_of_metadata_entries = nslf.popleft()

    child_nodes = []

    for _ in range(quantity_of_child_nodes):
        child_nodes.append(build_tree(nslf))

    metadata = []

    for _ in range(quantify_of_metadata_entries):
        metadata.append(nslf.popleft())

    return {
        "nodes": child_nodes,
        "metadata": metadata,
    }


tree = build_tree(nslf)


def sum_metadata(tree):
    return sum(tree["metadata"]) + sum(sum_metadata(node) for node in tree["nodes"])


part_1 = sum_metadata(tree)

print(part_1)


def get_value(tree):
    if len(tree["nodes"]) == 0:
        return sum(tree["metadata"])

    value = 0

    for index in tree["metadata"]:
        if index <= len(tree["nodes"]):
            value += get_value(tree["nodes"][index - 1])

    return value


part_2 = get_value(tree)

print(part_2)
