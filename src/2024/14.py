import pathlib
from collections import namedtuple
from functools import reduce

from PIL import Image
from utils import *

data = pathlib.Path("../../data/2024/14.txt").read_text(encoding="utf-8")
lines = data.strip().split("\n")

WIDTH = 101
HEIGHT = 103
TILES_X = 120
TILES_Y = 120

Robot = namedtuple("Robot", ["px", "py", "vx", "vy"])

robots = [Robot(*ints(line)) for line in lines]

img = Image.new("RGB", (WIDTH * TILES_X, HEIGHT * TILES_Y), "white")
pixels = img.load()

elapsed = 0

for ty in range(0, TILES_Y):
    for tx in range(0, TILES_X):
        for i, robot in enumerate(robots):
            nx = (robot.px + (robot.vx + WIDTH)) % WIDTH
            ny = (robot.py + (robot.vy + HEIGHT)) % HEIGHT

            robots[i] = Robot(nx, ny, robot.vx, robot.vy)

        elapsed += 1

        if elapsed == 100:
            mx = WIDTH // 2
            my = HEIGHT // 2

            quadrants = [0] * 4

            for robot in robots:
                px = robot.px
                py = robot.py

                if px < mx and py < my:
                    quadrants[0] += 1
                elif px < mx and py > my:
                    quadrants[1] += 1
                elif px > mx and py < my:
                    quadrants[2] += 1
                elif px > mx and py > my:
                    quadrants[3] += 1

            part_1 = reduce(lambda m, n: m * n, quadrants, 1)

            print(part_1)

        part_2 = 7623  # value manually calculated based on the generated image: 120 * math.floor(mouse_y / 103) + math.ceil(mouse_x / 101)

        if elapsed == 7623:
            for xx in range(WIDTH):
                for yy in range(HEIGHT):
                    pixels[tx * WIDTH + xx, ty * HEIGHT + yy] = (0, 255, 0)

        for robot in robots:
            pixels[tx * WIDTH + robot.px, ty * HEIGHT + robot.py] = (0, 0, 0)

img.save("robots.png", "PNG")
