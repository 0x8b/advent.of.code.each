import operator
import pathlib

from utils import *

data = pathlib.Path("../../data/2024/15.txt").read_text(encoding="utf-8")
warehouse, moves = data.strip().split("\n\n")

warehouse = matrix(warehouse.strip(), separator="")
moves = list("".join(moves.strip().split("\n")))

wider_warehouse = []

for row in range(len(warehouse)):
    wider_warehouse.append(
        list(
            "".join(
                [
                    {"#": "##", "O": "[]", "@": "@.", ".": ".."}[c]
                    for c in warehouse[row]
                ]
            )
        )
    )

move_map = {
    "^": [-1, 0],
    ">": [0, 1],
    "v": [1, 0],
    "<": [0, -1],
}


def find_robot(warehouse):
    for row in range(len(warehouse)):
        for col in range(len(warehouse[0])):
            if warehouse[row][col] == "@":
                return row, col


robot_row, robot_col = find_robot(warehouse)

for move in moves:
    mr, mc = move_map[move]

    new_robot_row, new_robot_col = robot_row + mr, robot_col + mc

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
            rr = new_robot_row + count * mr
            rc = new_robot_col + count * mc

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
        warehouse[new_robot_row][new_robot_col] = "@"

        robot_row = new_robot_row
        robot_col = new_robot_col

        for c in range(1, count + 1):
            warehouse[new_robot_row + c * mr][new_robot_col + c * mc] = "O"


part_1 = 0

for row in range(len(warehouse)):
    for col in range(len(warehouse[0])):
        if warehouse[row][col] == "O":
            part_1 += 100 * row + col

print(part_1)


def can_move_boxes_vertically(warehouse, br, bc, mr):
    movable_boxes = []

    def can_move_vertically(warehouse, br, bc, mr):
        movable_boxes.extend([((br, bc), "["), ((br, bc + 1), "]")])

        match [warehouse[br + mr][bc], warehouse[br + mr][bc + 1]]:
            case [".", "."]:
                return True

            case ["[", "]"]:
                return can_move_vertically(warehouse, br + mr, bc, mr)

            case [".", "["]:
                return can_move_vertically(warehouse, br + mr, bc + 1, mr)

            case ["]", "."]:
                return can_move_vertically(warehouse, br + mr, bc - 1, mr)

            case ["]", "["]:
                return can_move_vertically(
                    warehouse, br + mr, bc - 1, mr
                ) and can_move_vertically(warehouse, br + mr, bc + 1, mr)

            case _:
                return False

    return movable_boxes if can_move_vertically(warehouse, br, bc, mr) else False


def can_move_boxes_horizontally(warehouse, rr, rc, mc):
    movable_boxes = []

    def can_move_horizontally(warehouse, rr, rc, mc):
        if warehouse[rr][rc] == "#":
            return False

        if warehouse[rr][rc] == ".":
            return True

        if mc == -1 and warehouse[rr][rc] == "]":
            movable_boxes.extend([((rr, rc), "]"), ((rr, rc - 1), "[")])

            return can_move_horizontally(warehouse, rr, rc - 2, mc)

        if mc == 1 and warehouse[rr][rc] == "[":
            movable_boxes.extend([((rr, rc), "["), ((rr, rc + 1), "]")])

            return can_move_horizontally(warehouse, rr, rc + 2, mc)

    return movable_boxes if can_move_horizontally(warehouse, rr, rc + mc, mc) else False


def can_move_boxes(warehouse, robot_row, robot_col, mr, mc):
    if mr == 0:
        return can_move_boxes_horizontally(warehouse, robot_row, robot_col, mc)

    if mc == 0:
        box_col = (
            robot_col + mc
            if warehouse[robot_row + mr][robot_col + mc] == "["
            else robot_col + mc - 1
        )
        box_row = robot_row + mr

        return can_move_boxes_vertically(warehouse, box_row, box_col, mr)


def move_boxes(warehouse, mr, mc, old_positions):
    for (box_row, box_col), _ in old_positions:
        warehouse[box_row][box_col] = "."

    for (box_row, box_col), char in old_positions:
        warehouse[box_row + mr][box_col + mc] = char


robot_row, robot_col = find_robot(wider_warehouse)

for move in moves:
    mr, mc = move_map[move]

    robot_next_row, robot_next_col = robot_row + mr, robot_col + mc

    if wider_warehouse[robot_next_row][robot_next_col] == ".":
        wider_warehouse[robot_row][robot_col] = "."
        wider_warehouse[robot_next_row][robot_next_col] = "@"

        robot_row, robot_col = robot_next_row, robot_next_col

    elif wider_warehouse[robot_next_row][robot_next_col] == "#":
        continue

    elif wider_warehouse[robot_next_row][robot_next_col] in ["[", "]"]:
        if box_positions := can_move_boxes(
            wider_warehouse, robot_row, robot_col, mr, mc
        ):
            move_boxes(wider_warehouse, mr, mc, box_positions)

            wider_warehouse[robot_row][robot_col] = "."
            wider_warehouse[robot_next_row][robot_next_col] = "@"

            robot_row, robot_col = robot_next_row, robot_next_col

part_2 = 0

for row in range(len(wider_warehouse)):
    for col in range(len(wider_warehouse[0])):
        if wider_warehouse[row][col] == "[":
            part_2 += 100 * row + col

print(part_2)

assert part_1 == 1479679
assert part_2 == 1509780
