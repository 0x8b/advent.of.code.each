#!/usr/bin/env python

import asyncio
import datetime
import json
import os
import pathlib
import re
import sys
import time

import requests
from dotenv import find_dotenv, load_dotenv

_ = load_dotenv(find_dotenv())


def download_title(year, day):
    url = f"https://adventofcode.com/{year}/day/{day}"

    response = requests.get(url)

    if response.status_code != 200:
        return None

    html_content = response.text

    pattern = re.compile(rf"--- Day {day}: (.*?) ---", re.IGNORECASE)
    match = pattern.search(html_content)

    if match:
        puzzle = match.group(1).strip().replace("&apos;", "'")

        meta_file = pathlib.Path("meta.json")

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
    response = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input",
        cookies={"session": os.environ["SESSION"]},
    )

    if response.status_code != 200:
        return None

    pathlib.Path(f"data/{year}/{str(day).zfill(2)}.txt").write_text(
        response.text.strip(), encoding="utf-8"
    )

    print(f"Zapisano dane wejściowe dla {year} {day}")


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

            time.sleep(3)


def download_specific(year: int, day: int):
    download_input(year, day)
    download_title(year, day)


def download_today():
    today = datetime.date.today()

    if today.month == 12 and today.day <= 25:
        download_input(today.year, today.day)
        download_title(today.year, today.day)


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
        case _:
            sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
