import pathlib
from collections import defaultdict

from utils import *

data = pathlib.Path("../../data/2015/19.txt").read_text(encoding="utf-8")
replacements_lines, molecule = data.strip().split("\n\n")

replacements = defaultdict(list)

for line in replacements_lines.split("\n"):
    e, m = line.split(" => ")

    replacements[e].append(m)

molecule_elements = []

for ch in molecule:
    if ch.isupper():
        molecule_elements.append(ch)
    else:
        molecule_elements[-1] = molecule_elements[-1] + ch

unique_molecules = set()

for i, element in enumerate(molecule_elements):
    if element not in replacements:
        continue

    for replacement in replacements[element]:
        new_molecule = "".join(
            molecule_elements[:i] + [replacement] + molecule_elements[i + 1 :]
        )

        unique_molecules.add(new_molecule)


part_1 = len(unique_molecules)

print(part_1)
