#!/usr/bin/env python3
import re
from itertools import product

def part_one(x1, x2, y1, y2):
    max_y_all = 0
    for vx, vy in product(range(x2+1), range(y1, abs(y1))):
        px = py = max_y = 0
        while True:
            px += vx
            py += vy
            max_y = max(max_y, py)
            vx = max(vx-1, 0)
            vy -= 1
            if x1<=px<=x2 and y1<=py<=y2:
                max_y_all = max(max_y_all, max_y)
                break
            if (vx == 0 and px < x1) or (px > x2) or (py < y2):
                break
    return max_y_all

def part_two(x1, x2, y1, y2):
    landed = 0
    for vx, vy in product(range(x2+1), range(y1, abs(y1))):
        px = py = 0
        while True:
            px += vx
            py += vy
            vx = max(vx-1, 0)
            vy -= 1
            if x1<=px<=x2 and y1<=py<=y2:
                landed += 1
                break
            if (vx == 0 and px < x1) or (px > x2) or (py < y1):
                break
    return landed

if __name__ == "__main__":
    input_path = "day-17/input.txt"
    with open(input_path) as f:
        x1, x2, y1, y2 = map(int, re.findall(r'-?\d+', f.readline().strip()))
    print("Part 1")
    print(part_one(x1, x2, y1, y2))
    print("Part 2")
    print(part_two(x1, x2, y1, y2))