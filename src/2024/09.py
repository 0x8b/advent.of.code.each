import pathlib
from dataclasses import dataclass

from utils import *

data = pathlib.Path("../../data/2024/09.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")


@dataclass
class File:
    id: int
    blocks: int
    moved: bool

    def as_moved(self):
        return File(id=self.id, blocks=self.blocks, moved=True)


@dataclass
class FreeSpace:
    blocks: int


disk = [
    (
        File(id=(i // 2), blocks=blocks, moved=False)
        if i % 2 == 0
        else FreeSpace(blocks=blocks)
    )
    for i, blocks in enumerate(digits(lines[0]))
]


def get_real_disk(disk):
    real_disk = []

    for fragment in disk:
        if isinstance(fragment, File):
            real_disk.extend([fragment.id] * fragment.blocks)
        else:
            real_disk.extend([None] * fragment.blocks)

    return real_disk


real_disk = get_real_disk(disk)
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

current_file_id = disk[-1].id

while current_file_id > 0:
    file_index = next(
        (
            i
            for i, blocks in enumerate(disk)
            if isinstance(blocks, File)
            and blocks.id == current_file_id
            and not blocks.moved
        ),
        -1,
    )

    for blocks_index, blocks in enumerate(disk):
        if blocks_index < file_index:
            if isinstance(blocks, FreeSpace):
                space_index = blocks_index

                if disk[file_index].blocks <= disk[space_index].blocks:
                    if disk[file_index].blocks < disk[space_index].blocks:
                        moved_file = disk[file_index].as_moved()

                        disk[file_index] = FreeSpace(blocks=moved_file.blocks)
                        disk[space_index : space_index + 1] = [
                            moved_file,
                            FreeSpace(
                                blocks=disk[space_index].blocks - moved_file.blocks
                            ),
                        ]
                    else:
                        [disk[space_index], disk[file_index]] = [
                            disk[file_index].as_moved(),
                            disk[space_index],
                        ]

                    break
        else:
            break

    current_file_id -= 1


part_2 = sum(
    i * file_id for i, file_id in enumerate(get_real_disk(disk)) if file_id is not None
)

print(part_2)
