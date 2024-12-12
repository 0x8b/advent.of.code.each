import pathlib

lines = (
    pathlib.Path("../../data/2019/01.txt")
    .read_text(encoding="utf-8")
    .strip()
    .split("\n")
)

masses = [int(line) for line in lines]


def calculate_fuel(mass):
    return mass // 3 - 2


part_1 = 0
part_2 = 0

for mass in masses:
    part_1 += mass // 3 - 2

    while True:
        fuel = calculate_fuel(mass)

        if fuel > 0:
            part_2 += fuel
            mass = fuel
        else:
            break

print(part_1)
print(part_2)
