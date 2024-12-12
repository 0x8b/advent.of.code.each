#!/usr/bin/env python

import asyncio
import datetime
import functools
import itertools
import json
import operator
import os
import pathlib
import re
import sys
import time
from collections import defaultdict
from pathlib import Path

import requests
from dotenv import find_dotenv, load_dotenv
from jinja2 import Environment, FileSystemLoader

_ = load_dotenv(find_dotenv())


def download_title(year, day):
    meta_file = pathlib.Path("meta.json")

    if not meta_file.is_file():
        meta_file.write_text(json.dumps({"days": {}}, indent=2))

    try:
        days = json.loads(meta_file.read_text())["days"]

        if f"{year}/{str(day).zfill(2)}" in days.keys():
            return

    except Exception as exc:
        print(exc)
        return

    url = f"https://adventofcode.com/{year}/day/{day}"

    response = requests.get(url)

    if response.status_code != 200:
        return None

    html_content = response.text

    pattern = re.compile(rf"--- Day {day}: (.*?) ---", re.IGNORECASE)
    match = pattern.search(html_content)

    if match:
        puzzle = match.group(1).strip().replace("&apos;", "'")

        meta_file.write_text(
            json.dumps(
                {
                    "days": dict(
                        list(
                            sorted(
                                list(
                                    json.loads(meta_file.read_text(encoding="utf-8"))[
                                        "days"
                                    ].items()
                                )
                                + [(f"{year}/{str(day).zfill(2)}", puzzle)]
                            )
                        )
                        + []
                    )
                },
                indent=2,
            ),
            encoding="utf-8",
        )

        print(f"Zaktualizowano plik meta.json o dane z {year} {day}")


def download_input(year, day):
    directory = pathlib.Path(f"data/{year}")

    if not directory.is_dir():
        directory.mkdir(parents=True, exist_ok=True)

    input_file = pathlib.Path(f"data/{year}/{str(day).zfill(2)}.txt")

    if input_file.is_file() and len(input_file.read_text().strip()):
        return

    response = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input",
        cookies={"session": os.environ["SESSION"]},
    )

    if response.status_code != 200:
        return None

    input_file.write_text(response.text.strip(), encoding="utf-8")

    print(f"Zapisano dane wejściowe dla {year} {day}")


def copy_solution_template(year, day):
    template = pathlib.Path("day.template.py")
    target = pathlib.Path(f"src/{year}/{str(day).zfill(2)}.py")

    if target.is_file() and len(target.read_text()):
        return

    target.write_text(
        template.replace("YYYY", str(year)).replace("DD", str(day).zfill(2)),
        encoding="utf-8",
    )


def download_all():
    today = datetime.date.today()

    for year in range(2015, 3000):
        if year > today.year:
            break

        for day in range(1, 26):
            if year == today.year and day > today.day:
                break

            download_input(year, day)
            download_title(year, day)
            copy_solution_template(year, day)

            time.sleep(3)


def download_specific(year: int, day: int):
    download_input(year, day)
    download_title(year, day)
    copy_solution_template(year, day)


def download_today():
    today = datetime.date.today()

    if today.month == 12 and today.day <= 25:
        download_input(today.year, today.day)
        download_title(today.year, today.day)
        copy_solution_template(today.year, today.day)


def collect_data_for_readme():
    meta = json.loads(Path("meta.json").read_text())

    extension_to_language = {
        "py": "Python",
        "rb": "Ruby",
    }

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
            f"[{extension_to_language[extension]}]({link})"
            for extension, link in sorted(
                events[year][day]["solutions"], key=operator.itemgetter(0)
            )
        )

        source_code = solution.read_text(encoding="utf-8")

        events[year][day]["progress"] = max(
            events[year][day]["progress"],
            sum(("part_1" in source_code, "part_2" in source_code)),
        )

    emojis = dict(
        zip(
            [str(year) for year in range(2015, 2030)],
            itertools.cycle(["🎅", "🦌", "🍪", "🎁", "🎄"]),
        )
    )

    stars = defaultdict(int)
    solved = defaultdict(int)

    for year in events:
        for day in events[year]:
            stars[year] += events[year][day]["progress"]
            solved[year] += 1 if events[year][day]["progress"] == 2 else 0

    return {
        "range": f"{min(events.keys())}-{max(events.keys())}",
        "events": events,
        "emojis": emojis,
        "stars": stars,
        "solved": solved,
    }


def render_readme(data, template_file, output_file):
    env = Environment(loader=FileSystemLoader(os.path.dirname(template_file)))
    template = env.get_template(os.path.basename(template_file))

    Path(output_file).write_text(template.render(data), encoding="utf-8")


async def main():
    if len(sys.argv) < 2:
        sys.exit(1)

    command = sys.argv[1]

    match command:
        case "download":
            match sys.argv[2:]:
                case "all":
                    download_all()
                case year, day if True:
                    download_specific(year, day)
                case "today":
                    download_today()
                case _:
                    raise SystemExit(
                        "Unknown command. Usage: ./aoc.py download <all|year day|today>"
                    )
        case "render":
            render_readme(collect_data_for_readme(), "README.md.jinja", "README.md")
        case _:
            sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
