import hashlib
import pathlib

from utils import *

data = pathlib.Path("../../data/2016/05.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

door_id = lines[0]

password = ""
i = 0

while len(password) != 8:
    h = hashlib.new("md5")
    h.update(bytes(f"{door_id}{i}", "utf-8"))
    digest = h.hexdigest()

    if digest.startswith("00000") and digest[5] != "0":
        password += digest[5]

    i += 1

part_1 = password

print(part_1)


password = [None] * 8
i = 0

while True:
    h = hashlib.new("md5")
    h.update(bytes(f"{door_id}{i}", "utf-8"))
    digest = h.hexdigest()

    if digest.startswith("00000") and digest[5].isdigit():
        index = int(digest[5])

        if 0 <= index < 8 and not password[index]:
            password[index] = digest[6]

        if None not in password:
            break

    i += 1

part_2 = "".join(password)

print(part_2)
