import operator
import pathlib

from utils import *

data = pathlib.Path("../../data/2024/15.txt").read_text(encoding="utf-8")
warehouse, moves = data.strip().split("\n\n")

warehouse = matrix(warehouse.strip(), separator="")
moves = list("".join(moves.strip().split("\n")))

warehouse_copy = [[c for c in row] for row in warehouse]


for row in range(len(warehouse)):
    for col in range(len(warehouse[0])):
        if warehouse[row][col] == "@":
            robot_row = row
            robot_col = col
            break


moving_map = {
    "^": [-1, 0],
    ">": [0, 1],
    "v": [1, 0],
    "<": [0, -1],
}


for move in moves:
    move_row = moving_map[move][0]
    move_col = moving_map[move][1]

    new_robot_row = robot_row + move_row
    new_robot_col = robot_col + move_col

    if warehouse[new_robot_row][new_robot_col] == "#":
        continue
    elif warehouse[new_robot_row][new_robot_col] == ".":
        warehouse[robot_row][robot_col] = "."

        robot_row = new_robot_row
        robot_col = new_robot_col
        warehouse[robot_row][robot_col] = "@"

    elif warehouse[new_robot_row][new_robot_col] == "O":
        count = 0

        while True:
            rr = new_robot_row + count * move_row
            rc = new_robot_col + count * move_col

            if warehouse[rr][rc] == "#":
                count = -1
                break
            elif warehouse[rr][rc] == ".":
                break
            elif warehouse[rr][rc] == "O":
                count += 1

        if count <= 0:
            continue

        warehouse[robot_row][robot_col] = "."
        robot_row = new_robot_row
        robot_col = new_robot_col
        warehouse[robot_row][robot_col] = "@"

        for c in range(1, count + 1):
            warehouse[new_robot_row + c * move_row][new_robot_col + c * move_col] = "O"


part_1 = 0

for row in range(len(warehouse)):
    for col in range(len(warehouse[0])):
        if warehouse[row][col] == "O":
            part_1 += 100 * row + col

print(part_1)


warehouse = []

for row in range(len(warehouse_copy)):
    new_row = list(
        "".join(
            [
                {"#": "##", "O": "[]", "@": "@.", ".": ".."}[c]
                for c in warehouse_copy[row]
            ]
        )
    )

    warehouse.append(new_row)

for row in range(len(warehouse)):
    for col in range(len(warehouse[0])):
        if warehouse[row][col] == "@":
            robot_row = row
            robot_col = col
            break


def can_push_boxes_vertically(warehouse, br, bc, mr):
    boxes = []

    def rec(warehouse, br, bc, mr):
        boxes.extend([((br, bc), "["), ((br, bc + 1), "]")])

        if warehouse[br + mr][bc] == "." and warehouse[br + mr][bc + 1] == ".":
            return True

        if warehouse[br + mr][bc] == "[" and warehouse[br + mr][bc + 1] == "]":
            can_push = rec(warehouse, br + mr, bc, mr)

            if can_push:
                boxes.extend([((br + mr, bc), "["), ((br + mr, bc + 1), "]")])

            return can_push

        if warehouse[br + mr][bc] == "." and warehouse[br + mr][bc + 1] == "[":
            can_push = rec(warehouse, br + mr, bc + 1, mr)

            if can_push:
                boxes.extend([((br + mr, bc + 1), "["), ((br + mr, bc + 2), "]")])

            return can_push

        if warehouse[br + mr][bc] == "]" and warehouse[br + mr][bc + 1] == ".":
            can_push = rec(warehouse, br + mr, bc - 1, mr)

            if can_push:
                boxes.extend([((br + mr, bc - 1), "["), ((br + mr, bc), "]")])

            return can_push

        if warehouse[br + mr][bc] == "]" and warehouse[br + mr][bc + 1] == "[":
            can_push = rec(warehouse, br + mr, bc - 1, mr) and rec(
                warehouse, br + mr, bc + 1, mr
            )

            if can_push:
                boxes.extend(
                    [
                        ((br + mr, bc - 1), "["),
                        ((br + mr, bc), "]"),
                        ((br + mr, bc + 1), "["),
                        ((br + mr, bc + 2), "]"),
                    ]
                )

            return can_push

        return False

    if rec(warehouse, br, bc, mr):
        return boxes
    else:
        return False


def can_push_boxes(warehouse, rr, rc, mr, mc):
    if mr == 0:
        # push horizontally

        count = 0

        while warehouse[rr + (count + 1) * mr][rc + (count + 1) * mc] not in ["#", "."]:
            count += 1

        if count == 0:
            return False

        if warehouse[rr + (count + 1) * mr][rc + (count + 1) * mc] == "#":
            return False

        boxes = []

        for c in range(1, count + 1):
            boxes.append(((rr, rc + c * mc), warehouse[rr][rc + c * mc]))

        return sorted(boxes, key=operator.itemgetter(0))

    if mc == 0:
        # push vertically

        bc = rc + mc if warehouse[rr + mr][rc + mc] == "[" else rc + mc - 1
        br = rr + mr

        return can_push_boxes_vertically(warehouse, br, bc, mr)


def push_boxes(warehouse, rr, rc, mr, mc, old):
    for (r, c), _ in old:
        warehouse[r][c] = "."

    for (r, c), ch in old:
        warehouse[r + mr][c + mc] = ch


for move_i, move in enumerate(moves, 1):
    move_row = moving_map[move][0]
    move_col = moving_map[move][1]

    if warehouse[robot_row + move_row][robot_col + move_col] == ".":
        warehouse[robot_row][robot_col] = "."

        robot_row = robot_row + move_row
        robot_col = robot_col + move_col

        warehouse[robot_row][robot_col] = "@"
    elif warehouse[robot_row + move_row][robot_col + move_col] == "#":
        continue
    elif warehouse[robot_row + move_row][robot_col + move_col] in ["[", "]"]:
        if coords := can_push_boxes(
            warehouse, robot_row, robot_col, move_row, move_col
        ):
            push_boxes(warehouse, robot_row, robot_col, move_row, move_col, coords)
            warehouse[robot_row + move_row][robot_col + move_col] = "@"
            warehouse[robot_row][robot_col] = "."
            robot_row = robot_row + move_row
            robot_col = robot_col + move_col

part_2 = 0

for row in range(len(warehouse)):
    for col in range(len(warehouse[0])):
        if warehouse[row][col] == "[":
            part_2 += 100 * row + col

print(part_2)
