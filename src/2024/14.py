import pathlib
from collections import namedtuple
from functools import reduce

from PIL import Image
from utils import *

data = pathlib.Path("../../data/2024/14.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

WIDTH = 101
HEIGHT = 103


Robot = namedtuple("Robot", ["id", "px", "py", "vx", "vy"])

robots = [Robot(i, *ints(line)) for i, line in enumerate(lines)]

img = Image.new("RGB", (WIDTH * 120, HEIGHT * 120), "white")

pixels = img.load()

elapsed = 0

for y in range(0, 120):
    for x in range(0, 120):
        for i, robot in enumerate(robots):
            nx = (robot.px + (robot.vx + WIDTH)) % WIDTH
            ny = (robot.py + (robot.vy + HEIGHT)) % HEIGHT

            nrobot = Robot(robot.id, nx, ny, robot.vx, robot.vy)

            robots[i] = nrobot

        elapsed += 1

        if elapsed == 100:
            mx = WIDTH // 2
            my = HEIGHT // 2
            quadrants = [0] * 4

            for robot in robots:
                match robot:
                    case Robot(_, px, py, _, _) if px < mx and py < my:
                        quadrants[0] += 1
                    case Robot(_, px, py, _, _) if px < mx and py > my:
                        quadrants[1] += 1
                    case Robot(_, px, py, _, _) if px > mx and py < my:
                        quadrants[2] += 1
                    case Robot(_, px, py, _, _) if px > mx and py > my:
                        quadrants[3] += 1

            part_1 = reduce(lambda m, n: m * n, quadrants, 1)

            print(part_1)

        part_2 = 7623  # manually calculated from the generated image

        if elapsed == 7623:
            for i in range(101):
                for j in range(103):
                    pixels[x * WIDTH + i, y * HEIGHT + j] = (0, 255, 0)

        for robot in robots:
            pixels[x * WIDTH + robot.px, y * HEIGHT + robot.py] = (0, 0, 0)

img.save("robots.png", "PNG")
