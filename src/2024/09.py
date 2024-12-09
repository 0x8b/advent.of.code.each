import itertools
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


def get_copy_of_disk():
    disk = [
        (
            File(id=(i // 2), blocks=blocks, moved=False)
            if i % 2 == 0
            else FreeSpace(blocks=blocks)
        )
        for i, blocks in enumerate(digits(lines[0]))
    ]

    return disk


def disk_to_blocks(disk):
    return list(
        itertools.chain.from_iterable(
            [getattr(fragment, "id", None)] * fragment.blocks for fragment in disk
        )
    )


def defragment_blocks(blocks):
    left = 0
    right = len(blocks) - 1

    while left < right:
        while blocks[left] is not None and left < right:
            left += 1

        while blocks[right] is None and left < right:
            right -= 1

        if left >= right:
            break

        [
            blocks[left],
            blocks[right],
        ] = [blocks[right], None]

    return blocks


def defragment_files(disk):
    current_file_id = disk[-1].id

    while current_file_id > 0:
        file_index = find_index(
            disk,
            lambda file: isinstance(file, File)
            and file.id == current_file_id
            and not file.moved,
        )

        for blocks_index, blocks in enumerate(disk):
            if blocks_index < file_index:
                if isinstance(blocks, FreeSpace):
                    space_index = blocks_index

                    space_blocks = disk[space_index].blocks
                    file_blocks = disk[file_index].blocks

                    if file_blocks <= space_blocks:
                        if file_blocks < space_blocks:
                            moved_file = disk[file_index].as_moved()

                            disk[file_index] = FreeSpace(blocks=file_blocks)
                            disk[space_index : space_index + 1] = [
                                moved_file,
                                FreeSpace(blocks=space_blocks - file_blocks),
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

    return disk


def checksum(real_disk):
    return sum(
        i * file_id for i, file_id in enumerate(real_disk) if file_id is not None
    )


part_1 = checksum(defragment_blocks(disk_to_blocks(get_copy_of_disk())))

print(part_1)

part_2 = checksum(disk_to_blocks(defragment_files(get_copy_of_disk())))

print(part_2)
