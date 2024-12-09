import pathlib

from utils import *

data = pathlib.Path("../../data/2024/09.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

disk_map = [
    (
        {"type": "file", "blocks": n, "moved": False}
        if i % 2 == 0
        else {"type": "free-space", "blocks": n}
    )
    for i, n in enumerate(digits(lines[0]))
]

file_id = 0

for fragment in disk_map:
    if fragment["type"] == "file":
        fragment["id"] = file_id

        file_id += 1


def get_real_disk(disk_map):
    real_disk = []

    for blocks in disk_map:
        if blocks["type"] == "file":
            real_disk.extend([blocks["id"]] * blocks["blocks"])
        else:
            real_disk.extend([None] * blocks["blocks"])

    return real_disk


real_disk = get_real_disk(disk_map)


left = 0
right = len(real_disk) - 1

while left < right:
    while real_disk[left] is not None and left < right:
        left += 1

    while real_disk[right] is None and left < right:
        right -= 1

    if left >= right:
        break

    real_disk[left] = real_disk[right]
    real_disk[right] = None

part_1 = sum(i * id for i, id in enumerate(real_disk) if id is not None)

print(part_1)


last_file_id = disk_map[-1]["id"]

while last_file_id > 0:
    file = next(
        (
            i
            for i, blocks in enumerate(disk_map)
            if "id" in blocks and blocks["id"] == last_file_id and not blocks["moved"]
        ),
        -1,
    )

    for space, blocks in enumerate(disk_map):
        if space < file:
            if blocks["type"] == "free-space":
                if disk_map[file]["blocks"] <= disk_map[space]["blocks"]:
                    if disk_map[file]["blocks"] == disk_map[space]["blocks"]:
                        disk_map[space] = {**disk_map[file], "moved": True}
                        disk_map[file] = {
                            "type": "free-space",
                            "blocks": disk_map[file]["blocks"],
                        }
                    else:
                        disk_map[space] = {
                            "type": "free-space",
                            "blocks": disk_map[space]["blocks"]
                            - disk_map[file]["blocks"],
                        }

                        moved_file = {
                            "type": "file",
                            "blocks": disk_map[file]["blocks"],
                            "id": disk_map[file]["id"],
                            "moved": True,
                        }
                        disk_map[file] = {
                            "type": "free-space",
                            "blocks": disk_map[file]["blocks"],
                        }
                        disk_map.insert(space, moved_file)  # file

                    break
        else:
            break

    last_file_id -= 1

real_disk = get_real_disk(disk_map)

part_2 = sum(i * file_id for i, file_id in enumerate(real_disk) if file_id is not None)

print(part_2)
