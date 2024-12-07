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

import concurrent.futures
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


def calculate(puzzle, guard_row, guard_col):
    direction = "up"

    rows = len(puzzle)
    cols = len(puzzle[0])

    visited = defaultdict(int)
    visited[(guard_row, guard_col)] += 1

    trace = [(guard_row, guard_col)]

    while True:
        try:
            guard_new_row = guard_row + vectors[direction]["row"]
            guard_new_col = guard_col + vectors[direction]["col"]

            if not (0 <= guard_new_row < rows and 0 <= guard_new_col < cols):
                break

            if puzzle[guard_new_row][guard_new_col] == "#":
                direction = direction_change[direction]
            else:
                guard_row = guard_new_row
                guard_col = guard_new_col

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
                    penultimate_index = rindex(trace[:-1], trace[last_index])
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

        except Exception:
            break

    return {
        "visited": visited,
        "cycle": False,
    }


result = calculate(puzzle, guard_row, guard_col).get("visited")

part_1 = len(list(value for value in result.values() if value != 0))

print(part_1)

obstructions = set(result.keys())


def analyze(puzzle, guard_row, guard_col, obstructions):
    count = 0

    for row, col in obstructions:
        if (row, col) == (guard_row, guard_col):
            continue

        puzzle_copy = [[c for c in r] for r in puzzle]
        puzzle_copy[row][col] = "#"

        if calculate(puzzle_copy, guard_row, guard_col).get("cycle"):
            count += 1

    return count


with concurrent.futures.ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
    batched_obstructions = list(
        itertools.batched(list(obstructions), len(obstructions) // os.cpu_count() + 1)
    )

    part_2 = sum(
        executor.map(
            analyze,
            [puzzle] * len(batched_obstructions),
            [guard_row] * len(batched_obstructions),
            [guard_col] * len(batched_obstructions),
            batched_obstructions,
        )
    )

    print(part_2)
