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

            match warehouse[rr][rc]:
                case "#":
                    count = -1
                    break
                case ".":
                    break
                case "O":
                    count += 1

        if count <= 0:
            continue

        warehouse[robot_row][robot_col] = "."
        warehouse[new_robot_row][new_robot_col] = "@"

        robot_row = new_robot_row
        robot_col = new_robot_col

        for c in range(1, count + 1):
            warehouse[new_robot_row + c * mr][new_robot_col + c * mc] = "O"


def score(warehouse, char):
    answer = 0

    for row in range(len(warehouse)):
        for col in range(len(warehouse[0])):
            if warehouse[row][col] == char:
                answer += 100 * row + col

    return answer


part_1 = score(warehouse, "O")

print(part_1)


def can_move_boxes_vertically(warehouse, br, bc, mr):
    movable_boxes = []

    def can_move_vertically(warehouse, br, bc, mr):
        movable_boxes.extend([((br, bc), "["), ((br, bc + 1), "]")])

        match warehouse[br + mr][bc], warehouse[br + mr][bc + 1]:
            case ".", ".":
                return True

            case "[", "]":
                return can_move_vertically(warehouse, br + mr, bc, mr)

            case ".", "[":
                return can_move_vertically(warehouse, br + mr, bc + 1, mr)

            case "]", ".":
                return can_move_vertically(warehouse, br + mr, bc - 1, mr)

            case "]", "[":
                return can_move_vertically(
                    warehouse, br + mr, bc - 1, mr
                ) and can_move_vertically(warehouse, br + mr, bc + 1, mr)

            case _:
                return False

    return movable_boxes if can_move_vertically(warehouse, br, bc, mr) else False


def can_move_boxes_horizontally(warehouse, rr, rc, mc):
    movable_boxes = []

    def can_move_horizontally(warehouse, rr, rc, mc):
        match warehouse[rr][rc]:
            case "#":
                return False

            case ".":
                return True

            case "]" if mc == -1:
                movable_boxes.extend([((rr, rc), "]"), ((rr, rc - 1), "[")])

                return can_move_horizontally(warehouse, rr, rc - 2, mc)

            case "[" if mc == 1:
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

part_2 = score(wider_warehouse, "[")

print(part_2)
