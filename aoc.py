import datetime
import os
import pathlib
import re
import time

import requests
from dotenv import find_dotenv, load_dotenv

_ = load_dotenv(find_dotenv())


def get_day_title(year, day):
    url = f"https://adventofcode.com/{year}/day/{day}"

    response = requests.get(url)
    if response.status_code != 200:
        return None

    html_content = response.text

    pattern = re.compile(rf"--- Day {day}: (.*?) ---", re.IGNORECASE)
    match = pattern.search(html_content)

    if match:
        return match.group(1).strip().replace("&apos;", "'")
    else:
        return None


def get_input(year, day):
    cookies = {"session": os.environ["SESSION"]}

    response = requests.get(
        f"https://adventofcode.com/{year}/day/{day}/input", cookies=cookies
    )

    if response.status_code != 200:
        return None

    return response.text


def download_all_inputs():
    today = datetime.date.today()

    current_year = today.year
    current_day = today.day

    for year in range(2015, 3000):
        if year > current_year:
            break

        for day in range(1, 26):
            if year == current_year and day > current_day:
                break

            input_file = pathlib.Path(f"data/{year}/{str(day).zfill(2)}.txt")

            if input_file.exists() and input_file.read_text().strip():
                continue

            input_file.write_text(get_input(year, day), encoding="utf-8")

            print(f"<- {input_file}")

            time.sleep(3)
