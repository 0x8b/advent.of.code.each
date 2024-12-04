import pathlib

data = pathlib.Path("../../data/2024/04.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

grid = [list(line) for line in lines]


def search_xmas(grid, matches, traces):
    count = 0

    gw = len(grid[0])
    gh = len(grid)

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            for trace in traces:
                trace = [[x + t[0], y + t[1]] for t in trace]
                trace = [t for t in trace if 0 <= t[0] < gw and 0 <= t[1] < gh]

                if "".join([grid[ty][tx] for [tx, ty] in trace]) in matches:
                    count += 1

    return count


part_1 = search_xmas(
    grid,
    ["XMAS"],
    [
        [[0, 0], [1, 0], [2, 0], [3, 0]],
        [[0, 0], [-1, 0], [-2, 0], [-3, 0]],
        [[0, 0], [0, 1], [0, 2], [0, 3]],
        [[0, 0], [0, -1], [0, -2], [0, -3]],
        [[0, 0], [1, 1], [2, 2], [3, 3]],
        [[0, 0], [-1, -1], [-2, -2], [-3, -3]],
        [[0, 0], [1, -1], [2, -2], [3, -3]],
        [[0, 0], [-1, 1], [-2, 2], [-3, 3]],
    ],
)

part_2 = search_xmas(
    grid,
    ["AMSMS", "ASMMS", "AMSSM", "ASMSM"],
    [[[0, 0], [-1, -1], [1, 1], [-1, 1], [1, -1]]],
)

print(part_1)
print(part_2)
