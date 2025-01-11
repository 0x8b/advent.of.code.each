import pathlib
from itertools import accumulate, cycle, islice

from utils import *

data = pathlib.Path("../../data/2015/14.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

reindeers = []
max_distance = 0

for line in lines:
    name, speed, seconds, rest_seconds = (
        line.replace("can fly ", "")
        .replace("km/s for ", "")
        .replace("seconds, but then must rest for ", "")
        .replace(" seconds.", "")
        .split(" ")
    )

    speed, seconds, rest_seconds = int(speed), int(seconds), int(rest_seconds)

    reindeers.append((name, speed, seconds, rest_seconds))

    div, mod = divmod(2503, seconds + rest_seconds)

    distance = speed * div * seconds + speed * min(mod, seconds)

    max_distance = max(max_distance, distance)

part_1 = max_distance

print(part_1)


timelines = []

for name, speed, seconds, rest_seconds in reindeers:
    timeline = list(
        accumulate(islice(cycle([speed] * seconds + [0] * rest_seconds), 2503))
    )

    timelines.append(timeline)

points = [0] * len(timelines)

for distances in zip(*timelines):
    leading_distance = max(distances)

    for i in range(len(distances)):
        if distances[i] == leading_distance:
            points[i] += 1

part_2 = max(points)

print(part_2)
