#!/usr/bin/env python3
FORWARD, UP, DOWN = "forward", "up", "down"

def part_one(moves):
    x = y = 0
    for dir, val in moves:
        if dir == FORWARD: x += val
        if dir == UP: y -= val
        if dir == DOWN: y += val
    return x * y

def part_two(moves):
    x = y = aim = 0
    for dir, val in moves:
        if dir == FORWARD: x += val; y += aim * val
        if dir == UP: aim -= val
        if dir == DOWN: aim += val
    return x * y

if __name__ == "__main__":
    input_path = "day-02/input.txt"
    with open(input_path) as f:
        clean = lambda move: (move[0], int(move[1]))
        moves = list(map(lambda line: clean(line.strip().split()), f))
    print("Part 1")
    print(part_one(moves))
    print("Part 2")
    print(part_two(moves))
