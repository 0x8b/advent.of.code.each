import copy
import itertools
import operator
import pathlib

from utils import *

data = pathlib.Path("../../data/2024/07.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

equations = [ints(line) for line in lines]


def get_calibration_result(equations, operators):
    calibration_result = 0

    for [result, *operands] in equations:
        for operator_sequence in itertools.product(operators, repeat=len(operands) - 1):
            partial_result = operands[0]

            for i, op in enumerate(operator_sequence):
                partial_result = op(partial_result, operands[i + 1])

                if partial_result > result:
                    break

            if partial_result == result:
                calibration_result += result
                break

    return calibration_result


part_1 = get_calibration_result(equations, [operator.add, operator.mul])
part_2 = get_calibration_result(
    equations, [operator.add, operator.mul, lambda a, b: int(str(a) + str(b))]
)


print(part_1)
print(part_2)
