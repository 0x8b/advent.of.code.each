import hashlib
import pathlib

data = pathlib.Path("../../data/2015/04.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

secret_key = lines[0]


for leading_zeroes in [5, 6]:
    for i in range(1, 10000000000):
        h = hashlib.new("md5")
        h.update(bytes(f"{secret_key}{i}", encoding="utf-8"))

        if h.hexdigest().startswith("0" * leading_zeroes):
            print(i)  # part_1, part_2
            break
