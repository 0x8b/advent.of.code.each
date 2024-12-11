import functools
import json
import operator
import os
import re
from collections import defaultdict
from pathlib import Path

from jinja2 import Environment, FileSystemLoader


def collect_data():
    meta = json.loads(Path("meta.json").read_text())

    days = list(
        sorted(
            [(*yearday.split("/"), title) for yearday, title in meta["days"].items()],
            key=functools.cmp_to_key(
                lambda a, b: (
                    (int(a[1]) - int(b[1])) if a[0] == b[0] else int(b[0]) - int(a[0])
                )
            ),
        )
    )

    available_days = set(meta["days"].keys())

    events = defaultdict(lambda: defaultdict(lambda: dict()))

    for year, day, title in days:
        events[year][day] = {
            "title": f"[{title}](https://adventofcode.com/{year}/day/{int(day)})",
            "solutions": [],
            "solutions_formatted": "",
            "progress": 0,
        }

    for solution in [
        p
        for p in Path("src").rglob("*")
        if p.suffix in {".py", ".rb"} and "01" <= p.stem <= "25"
    ]:
        [year, day, extension] = re.findall(
            r"src\/(\d{4})\/(\d\d).(.*)", str(solution)
        ).pop()

        if f"{year}/{day}" not in available_days:
            continue

        events[year][day]["solutions"].append(
            [
                extension,
                f"https://github.com/0x8b/advent.of.code.each/blob/main/src/{year}/{day}.{extension}",
            ]
        )

        events[year][day]["solutions_formatted"] = ", ".join(
            f"[{extension}]({link})"
            for extension, link in sorted(
                events[year][day]["solutions"], key=operator.itemgetter(0)
            )
        )

        source_code = solution.read_text(encoding="utf-8")

        events[year][day]["progress"] = max(
            events[year][day]["progress"],
            sum(("part_1" in source_code, "part_2" in source_code)),
        )

    return {"range": f"{min(events.keys())}-{max(events.keys())}", "events": events}


def generate_report(data, template_file, output_file):
    env = Environment(loader=FileSystemLoader(os.path.dirname(template_file)))
    template = env.get_template(os.path.basename(template_file))

    Path(output_file).write_text(template.render(data), encoding="utf-8")


generate_report(collect_data(), "README.md.jinja", "README.md")
