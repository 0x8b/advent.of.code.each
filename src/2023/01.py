import pathlib

from utils import *

data = pathlib.Path("../../data/2023/01.txt").read_text(encoding="utf-8")
calibration_document = data.strip().split("\n")


calibration_values = [
    digits(line)[0] * 10 + digits(line)[-1] for line in calibration_document
]

part_1 = sum(calibration_values)

print(part_1)

letters_to_digit = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}

part_2 = 0

for line in calibration_document:
    domain = [key for key in letters_to_digit.keys() if key in line]

    part_2 += (
        letters_to_digit[min(domain, key=lambda letters: line.index(letters))] * 10
        + letters_to_digit[max(domain, key=lambda letters: line.rindex(letters))]
    )

print(part_2)
