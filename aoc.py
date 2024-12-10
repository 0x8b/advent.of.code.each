import re
import time

import requests


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


years = range(2015, 2025)
days = list(range(1, 26))

for year in years:
    for day in days:
        title = get_day_title(year, day)

        time.sleep(1)

        if title:
            print(f"{year}/{str(day).zfill(2)} {title}")
