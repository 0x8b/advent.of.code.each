import functools
import json
import operator
import os
from collections import defaultdict
from pathlib import Path

from jinja2 import Environment, FileSystemLoader


def analyze_directory():
    all_files = [
        p
        for p in Path("src").rglob("*")
        if p.suffix in {".py", ".rb"} and set(p.stem) < set("0123456789")
    ]

    meta = json.loads(Path("meta.json").read_text())

    days = list(
        sorted(
            [(*map(int, key.split("/")), value) for key, value in meta["days"].items()],
            key=functools.cmp_to_key(
                lambda a, b: (a[1] - b[1]) if a[0] == b[0] else b[0] - a[0]
            ),
        )
    )

    available_days = [f"{year}/{str(day).zfill(2)}" for (year, day, _) in days]

    years = defaultdict(lambda: defaultdict(lambda: dict()))

    for year, day, title in days:
        years[str(year)][str(day)] = {
            "title": f"[{title}](https://adventofcode.com/{year}/day/{day})",
            "solutions": [],
            "solutions_rendered": "",
            "progress": 0,
        }

    for file in all_files:
        content = file.read_text(encoding="utf-8")

        progress = 0

        if "part_1" in content:
            progress += 1

        if "part_2" in content:
            progress += 1

        [_, year, day] = str(file).split("/")

        [day, ext] = day.split(".")

        if f"{year}/{day}" not in available_days:
            continue

        day = day.lstrip("0")

        years[year][day]["solutions"].append(
            [
                ext,
                f"https://github.com/0x8b/advent.of.code.each/blob/main/src/{year}/{day.zfill(2)}.{ext}",
            ]
        )
        years[year][day]["solutions_rendered"] = ", ".join(
            f"[{ext}]({link})"
            for ext, link in sorted(
                years[year][day]["solutions"], key=operator.itemgetter(0)
            )
        )
        years[year][day]["progress"] = progress

    return {"events": "2015-2024", "years": years}


def generate_report(data, template_file, output_file):
    env = Environment(loader=FileSystemLoader(os.path.dirname(template_file)))
    template = env.get_template(os.path.basename(template_file))

    Path(output_file).write_text(template.render(data), encoding="utf-8")


generate_report(analyze_directory(), "README.md.jinja", "README.md")
