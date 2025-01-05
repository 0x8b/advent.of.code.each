import pathlib

data = pathlib.Path("../../data/2016/02.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")


keypad = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

keypad_2 = [
    [None, None, "1", None, None],
    [None, "2", "3", "4", None],
    ["5", "6", "7", "8", "9"],
    [None, "A", "B", "C", None],
    [None, None, "D", None, None],
]

row, col = 1, 1

dirs = dict([("U", (-1, 0)), ("D", (1, 0)), ("R", (0, 1)), ("L", (0, -1))])

part_1 = ""
part_2 = ""

for line in lines:
    for direction in line:
        r, c = row + dirs[direction][0], col + dirs[direction][1]

        if 0 <= r < 3 and 0 <= c < 3:
            row, col = r, c

    part_1 += keypad[row][col]


row, col = 2, 2

for line in lines:
    for direction in line:
        r, c = row + dirs[direction][0], col + dirs[direction][1]

        if 0 <= r < 5 and 0 <= c < 5 and keypad_2[r][c] is not None:
            row, col = r, c

    part_2 += keypad_2[row][col]

print(part_1)
print(part_2)
