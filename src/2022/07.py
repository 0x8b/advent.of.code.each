import collections
import pathlib
import uuid

from utils import *

data = pathlib.Path("../../data/2022/07.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

working_directory = []

STATS = {}


class File(collections.UserDict):
    def __init__(self, name, size):
        self.data = {}
        self.name = name
        self.size = int(size)


class Directory(collections.UserDict):
    def __init__(self, name):
        self.data = {}
        self.name = name
        self.size = 0
        self.uuid = str(uuid.uuid4())

    def calculate_size(self):
        size = 0

        for _, value in self.data.items():
            if isinstance(value, Directory):
                size += value.calculate_size()

            elif isinstance(value, File):
                size += value.size

        self.size = size

        STATS[self.uuid] = self.size

        return self.size


class Filesystem(collections.UserDict):
    def __init__(self):
        self.data = {}

    def __setitem__(self, path, item):
        cwd = self.data

        for directory in path[:-1]:
            if directory in cwd:
                cwd = cwd[directory]
            else:
                cwd[directory] = Directory(directory)
                cwd = cwd[directory]

        cwd[path[-1]] = item

        return cwd[path[-1]]

    def __getitem__(self, path):
        cwd = self.data

        for directory in path:
            cwd = cwd[directory]

        return cwd


filesystem = Filesystem()


for line in lines:
    match line.split(" "):
        case ["$", "cd", directory]:
            if directory == "..":
                working_directory.pop()
            else:
                working_directory.append(directory)

        case ["$", "ls"]:
            filesystem[working_directory] = Directory(working_directory[-1])

        case ["dir", directory]:
            filesystem[working_directory][directory] = Directory(directory)

        case [filesize, filename] if filesize.isdigit():
            filesystem[working_directory][filename] = File(filename, filesize)

        case other:
            raise ValueError(other)


filesystem[["/"]].calculate_size()

sizes = STATS.values()

part_1 = sum(size for size in sizes if size <= 100_000)

print(part_1)

total = max(sizes)

for size in sorted(sizes):
    if total - size <= 40_000_000:
        print(size)  # part_2
        break
