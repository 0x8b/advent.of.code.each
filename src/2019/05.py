import pathlib

from utils import *

data = pathlib.Path("../../data/2019/05.txt").read_text(encoding="utf-8")


for inp in [1, 5]:
    memory = ints(data.strip())
    ip = 0

    inputs = [inp]
    outputs = []

    def get_input():
        return inputs.pop(0)

    def print_output(value):
        outputs.append(value)

    def get_value(parameter, mode):
        if mode == 0:
            return memory[parameter]
        elif mode == 1:
            return parameter

    while ip < len(memory):
        modes = [
            None,
            memory[ip] % 1000 // 100,
            memory[ip] % 10000 // 1000,
            memory[ip] // 10000,
        ]
        opcode = memory[ip] % 100

        match opcode:
            case 1:
                parameter_1 = get_value(memory[ip + 1], modes[1])
                parameter_2 = get_value(memory[ip + 2], modes[2])

                memory[memory[ip + 3]] = parameter_1 + parameter_2

                ip += 4

            case 2:
                parameter_1 = get_value(memory[ip + 1], modes[1])
                parameter_2 = get_value(memory[ip + 2], modes[2])

                memory[memory[ip + 3]] = parameter_1 * parameter_2

                ip += 4

            case 3:
                memory[memory[ip + 1]] = get_input()

                ip += 2

            case 4:
                print_output(memory[memory[ip + 1]])

                ip += 2

            case 5:
                parameter_1 = get_value(memory[ip + 1], modes[1])
                parameter_2 = get_value(memory[ip + 2], modes[2])

                if parameter_1 != 0:
                    ip = parameter_2
                else:
                    ip += 3

            case 6:
                parameter_1 = get_value(memory[ip + 1], modes[1])
                parameter_2 = get_value(memory[ip + 2], modes[2])

                if parameter_1 == 0:
                    ip = parameter_2
                else:
                    ip += 3

            case 7:
                parameter_1 = get_value(memory[ip + 1], modes[1])
                parameter_2 = get_value(memory[ip + 2], modes[2])

                memory[memory[ip + 3]] = 1 if parameter_1 < parameter_2 else 0

                ip += 4

            case 8:
                parameter_1 = get_value(memory[ip + 1], modes[1])
                parameter_2 = get_value(memory[ip + 2], modes[2])

                memory[memory[ip + 3]] = 1 if parameter_1 == parameter_2 else 0

                ip += 4

            case 99:
                break

    if outputs:
        answer = outputs[-1]  # part_1, part_2

        print(answer)
