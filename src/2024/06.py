"""
:----======++++**%@@@##*#%%@@@%*#####################%%%%%%%%%%%%%%
:::------====++++%@@%**+#%%%%%*+###############################%%#+
::::-----=====+++@@@%*++#%%%%%*+##################################+
:::::-----=====++@@@#++=##%%%#=+***##%####**######################+
.::::------=====*@@%*==+#%%%%*-*%%@@@@@@@@@%%#***********########%*
.::::::-----====#@@%+==+##%%%%@@@@@@@@@@@@@@@@@@%************#####+
..::::::-----===#@@#+--*##%%@@@@%@@@@@@@@@@@@@@@@@@************##*=
....::::::----==%@%#=--*#%@@@@@%%@@@@%%%%%%%%%%@@@@@************#+=
.....:::::-----=%@%*-:-#%%@@@@@@@@@%%#+==***%@@@@@@@@**+*+*******==
....:::::----===@@%+:.-#%#%%@@@@@%#=.     ..+%%@@@@@@%++++++****+==
........:::::--=@%#=..=#%@@%%%%#+-....  .::.=#%%@@@@@@*+++++++**===
..........:::::+%%#-..+*=####=-::.......::::-*%@@@@@@@#++++++++*=--
   .........:::#%%+:..+: .:::::.  .......:::=*%@@@@@@@%+++++++++---
      ......:::%%#+. :+  .:....::.........:::-*%@@@@@@%++++++++----
         .....:%%#-:.:=:=**=--=+**=-...:::::---+@@@@@@%====++++-:--
            ..-%#*.=+==+*#%#***#####*+=======+#%@@@@@*=+=++====::--
              -%#+:%#%+=%%%%%#.*#%%%%%%@@%%%@@%=#%%*=###@@@@@@+-:::
              =##- -   -++#-.#:..=****#%:..:-=++*%#####%@@@@@@@@@@@
              +#*.  -:.      -#-.  .::-=.:-=====+**###*#@@@@@@@@@@@
              *#*    :***.   .:**=:::=-:-=======+**##**@@@@@@@@@@@@
              #**    :-++..::-::+**+========-==++**==*@@@@@@@@@@@@@
             :#*-   ==+#+=+**###==+**+========++**+++@@@@@@@@@@@@@@
             +#*. .+***##++*##+=-=+*##**++++++**##+=%@@@@@@@@@@@@@@
             ##*--**#####***#**###%%%%%####***#%%%@@@@@@@@@@@@@@@@@
            =*++#########*+*##*+=+=+#%##%%###%%%@@@@@@@@@@@@@@@@@@@
           +***#%%#%#####*=+*###*+++*#%%%%%%%@@@@@@@@@@@@@@@@@@@@@@
         .+###%%@%#######@=---:::-=*#%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@
         :*#%%%%@%#####%@@%*++=+*#%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
         +#@@@@@@@####%%@%%@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
         =%%@@@@@%##%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
         -%##@@@@%##%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
     .-::=#%%%@@@##%@%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
+**++-:-=*%%@@@@%##%@@@@@@@@@@@@ SZKODA GADAĆ @@@@@@@@@@@@@@@@@@@@%
:===-::...#%%%%@%###@@@@@@@@ SZKODA STRZĘPIĆ RYJA @@@@@@@@@@@@@@@@@
.         =%#%@@@%##%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
.......:-:*%@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""

import itertools
import os
import pathlib
from collections import defaultdict
from multiprocessing import Pool

from utils import *

data = pathlib.Path("../../data/2024/06.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

puzzle = matrix(lines, separator="", try_parse=True)

guard_row, guard_col = 0, 0


for i, row in enumerate(puzzle):
    try:
        guard_col = row.index("^")
        guard_row = i
    except Exception:
        pass

direction = "up"

direction_change = {
    "up": "right",
    "right": "down",
    "down": "left",
    "left": "up",
}

vectors = {
    "up": {"row": -1, "col": 0},
    "right": {"row": 0, "col": 1},
    "down": {"row": 1, "col": 0},
    "left": {"row": 0, "col": -1},
}


def calculate(puzzle, guard_row, guard_col, obstacle_row=-1, obstacle_col=-1):
    direction = "up"

    visited = defaultdict(int)
    visited[(guard_row, guard_col)] += 1

    trace = [(guard_row, guard_col)]

    while True:
        try:
            if not (
                0 <= guard_row + vectors[direction]["row"] < len(puzzle)
                and 0 <= guard_col + vectors[direction]["col"] < len(puzzle[0])
            ):
                break

            if (
                puzzle[guard_row + vectors[direction]["row"]][
                    guard_col + vectors[direction]["col"]
                ]
                == "#"
            ):
                direction = direction_change[direction]
            else:
                guard_row = guard_row + vectors[direction]["row"]
                guard_col = guard_col + vectors[direction]["col"]

                current_guard_position = (guard_row, guard_col)

                visited[current_guard_position] += 1

                trace.append(current_guard_position)

                if visited[current_guard_position] > 100:
                    return {
                        "visited": visited,
                        "cycle": False,
                    }

                if trace.count(current_guard_position) > 1:
                    last_index = len(trace) - 1
                    penultimate_index = trace.index(
                        trace[last_index], 0, last_index - 1
                    )
                    length = last_index - penultimate_index

                    if (
                        trace[penultimate_index - length + 1 : penultimate_index + 1]
                        == trace[penultimate_index + 1 : last_index + 1]
                        and length >= 4
                    ):
                        return {
                            "visited": visited,
                            "cycle": True,
                        }

            # if False:
            #     puzzle_copy = [[c for c in r] for r in puzzle]
            #     for r in range(len(puzzle_copy)):
            #         for c in range(len(puzzle_copy[0])):
            #             if (r, c) in visited:
            #                 puzzle_copy[r][c] = str(visited[(r, c)])
            #     puzzle_copy[obstacle_row][obstacle_col] = "@"

            #     print(len(trace), direction)
            #     print("\n".join("".join(row) for row in puzzle_copy))
            #     print("")

        except Exception:
            break

    return {
        "visited": visited,
        "cycle": False,
    }


# part_1 = len(
#     list(
#         value
#         for value in calculate(puzzle, guard_row, guard_col).get("visited").values()
#         if value != 0
#     )
# )

# print(part_1)


def analyze(puzzle, guard_row, guard_col, rows):
    count = 0

    for row in rows:
        for col in range(len(puzzle[0])):
            if (row, col) == (guard_row, guard_col):
                continue

            if puzzle[row][col] == ".":
                puzzle_copy = [[c for c in r] for r in puzzle]
                puzzle_copy[row][col] = "#"

                if calculate(puzzle_copy, guard_row, guard_col, row, col).get("cycle"):
                    count += 1

                    print((row, col), "CYCLE")
                else:
                    print((row, col))

    return count


if __name__ == "__main__":
    rows = list(
        itertools.batched(list(range(len(puzzle))), len(puzzle) // os.cpu_count() + 1)
    )

    input_data = [(puzzle, guard_row, guard_col, row) for row in rows]

    with Pool() as pool:
        results = pool.starmap(analyze, input_data)

        print(results)

        part_2 = sum(results)

        print(part_2)
