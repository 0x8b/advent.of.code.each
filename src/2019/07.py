import pathlib
from functools import reduce
from itertools import permutations

from utils import *

data = pathlib.Path("../../data/2019/07.txt").read_text(encoding="utf-8")

memory = data.strip()


class Intcode:
    def __init__(self, memory, inputs=None):
        self.memory = ints(memory.strip()) if isinstance(memory, str) else memory
        self.ip = 0
        self.inputs = [] if inputs is None else inputs
        self.outputs = []
        self.modes = [None] * 4
        self.paused = True


    def read(self):
        if self.inputs:
            return self.inputs.pop(0)
        else:
            self.paused = True


    def write(self, value):
        self.outputs.append(value)


    def value(self, param, mode):
        match mode:
            case 0:
                return self.memory[param]

            case 1:
                return param

            case _:
                raise ValueError("Unknown mode")


    def param(self, n):
        return self.value(self.memory[self.ip + n], self.modes[n])


    def run(self):
        self.paused = False

        while self.ip < len(self.memory) and not self.paused:
            self.modes = [
                None,
                self.memory[self.ip] % 1000 // 100,
                self.memory[self.ip] % 10000 // 1000,
                self.memory[self.ip] // 10000,
            ]

            opcode = self.memory[self.ip] % 100

            match opcode:
                case 1:
                    parameter_1 = self.param(1)
                    parameter_2 = self.param(2)

                    self.memory[self.memory[self.ip + 3]] = parameter_1 + parameter_2

                    self.ip += 4

                case 2:
                    parameter_1 = self.param(1)
                    parameter_2 = self.param(2)

                    self.memory[self.memory[self.ip + 3]] = parameter_1 * parameter_2

                    self.ip += 4

                case 3:
                    self.memory[self.memory[self.ip + 1]] = self.read()

                    self.ip += 2

                case 4:
                    self.write(self.memory[self.memory[self.ip + 1]])

                    self.ip += 2

                case 5:
                    parameter_1 = self.param(1)
                    parameter_2 = self.param(2)

                    if parameter_1 != 0:
                        self.ip = parameter_2
                    else:
                        self.ip += 3

                case 6:
                    parameter_1 = self.param(1)
                    parameter_2 = self.param(2)

                    if parameter_1 == 0:
                        self.ip = parameter_2
                    else:
                        self.ip += 3

                case 7:
                    parameter_1 = self.param(1)
                    parameter_2 = self.param(2)

                    self.memory[self.memory[self.ip + 3]] = 1 if parameter_1 < parameter_2 else 0

                    self.ip += 4

                case 8:
                    parameter_1 = self.param(1)
                    parameter_2 = self.param(2)

                    self.memory[self.memory[self.ip + 3]] = 1 if parameter_1 == parameter_2 else 0

                    self.ip += 4

                case 99:
                    break

        if self.outputs:
            answer = self.outputs[-1]

            return answer

        return None


part_1 = 0

for phases in permutations(range(5)):
    signal = reduce(lambda signal, phase: Intcode(memory, [phase, signal]).run(), phases, 0)

    part_1 = max(part_1, signal)

print(part_1)


part_2 = 0

for phases in permutations(range(5)):
    for phases_for_feedback_loop in permutations(range(5, 10)):

        # TODO: w jaki sposób spiąć inputy?


#     for phases_for_feedback_loop in permutations(range(5, 10)):
#         signal = reduce(lambda signal, phase: Intcode(memory, [phase, signal]).run(), phases + phases_for_feedback_loop, 0)

#         part_2 = max(part_2, signal)

#         # instances = [Intcode(memory) for _ in range(5)]

#         # output = 0

#         # for i in range(5):
#         #     output = instances[i].run([signals[i], output])

#         # part_1 = max(part_1, output)

#         # for i in range(5):
#         #     output = instances[i].run([signals_2[i], output])

#         # part_2 = max(part_2, output)

# print(part_1)
# print(part_2)
