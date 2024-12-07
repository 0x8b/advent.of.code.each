import concurrent.futures
import itertools
import operator
import os
import pathlib

from utils import *

data = pathlib.Path("../../data/2024/07.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

equations = [ints(line) for line in lines]

OPERATOR_MAP = {
    "add": operator.add,
    "mul": operator.mul,
    "concat": lambda a, b: int(str(a) + str(b)),
}


def get_calibration_result(equations, operator_names):
    operators = [OPERATOR_MAP[name] for name in operator_names]

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


def get_calibration_result_parallel(equations, operators):
    with concurrent.futures.ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
        batched_equations = list(
            itertools.batched(equations, len(equations) // os.cpu_count() + 1)
        )

        total = 0

        for partial in executor.map(
            get_calibration_result,
            batched_equations,
            [operators] * len(batched_equations),
        ):
            total += partial

        return total


part_1 = get_calibration_result_parallel(equations, ["add", "mul"])
part_2 = get_calibration_result_parallel(equations, ["add", "mul", "concat"])

print(part_1)
print(part_2)
