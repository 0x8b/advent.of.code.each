import hashlib
import pathlib
import re
from collections import defaultdict
from itertools import groupby

from utils import *

data = pathlib.Path("../../data/2016/14.txt").read_text(encoding="utf-8")

salt = data.strip()
salt = "abc"

nth_key = 0


keys = []

indices_for_three = defaultdict(list)
indices_for_five = defaultdict(list)

c = 0

for i in range(15_000_000):
    h = hashlib.new("md5")
    h.update(bytes(f"{salt}{i}", "utf-8"))

    digest = h.hexdigest()

    chunks = list("".join(g[1]) for g in groupby(digest))
    only_fives = [chunk for chunk in chunks if len(chunk) == 5]

    if only_fives:
        print(digest, i, chunks, only_fives)

    # if chunks:
    #     for chunk in chunks:
    #         if len(chunk) == 5:
    #             indices_for_five[chunk].append(i)

    #     if any(len(chunk) == 5 for chunk in chunks):
    #         for chunk in chunks:
    #             if len(chunk) == 5:
    #                 char = chunk[0]
    #                 c += 1
    #                 print(chunk, c)

    #                 # print(digest, char * 5, i)

    #                 for v in indices_for_three[char * 3]:
    #                     if v + 1 <= i <= v + 1000:
    #                         keys.append(v)

    #                         print(keys)

    #                         if len(keys) == 64:
    #                             break

    #                         break

    #     elif any(len(chunk) == 3 for chunk in chunks):
    #         for chunk in chunks:
    #             if len(chunk) == 3:
    #                 break

    #         char = chunk[0]

    #         # print(digest, char * 3, i)

    #         indices_for_three[char * 3].append(i)

    if i >= 42728:
        break
