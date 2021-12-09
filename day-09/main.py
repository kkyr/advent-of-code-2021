#!/usr/bin/env python3
from functools import reduce
from operator import mul

def part_one(board):
    lows = get_lows(board)
    return sum((board[y][x] for x, y in lows)) + len(lows)

def part_two(board):
    seen, basins, lows = set(), [], get_lows(board)
    for x, y in lows:
        basins.append(explore_basin(board, x, y, seen))
    return reduce(mul, sorted(basins)[-3:])

def get_lows(board):
    lows = []
    for j in range(len(board)):
        for i in range(len(board[0])):
            point = input[j][i]
            for x, y in get_adjacent(input, i, j):
                if input[y][x] <= input[j][i]: break
            else:
                lows.append((i, j))
    return lows

def get_adjacent(board, i, j):
    in_bounds = lambda x, y: x < len(board[0]) and x >= 0 and y < len(board) and y >= 0
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    return ((i - x, j - y) for (x, y) in dirs if in_bounds(i - x, j - y))

def explore_basin(board, i, j, seen):
    seen.add((i, j))
    size = 1
    for x, y in get_adjacent(board, i, j):
        if (x, y) not in seen and board[y][x] != 9:
            size += explore_basin(board, x, y, seen)
    return size

if __name__ == "__main__":
    input_path = "day-09/input.txt"
    with open(input_path) as f:
        input = [[int(x) for x in line] for line in f.read().splitlines()]
    print("Part 1")
    print(part_one(input))
    print("Part 2")
    print(part_two(input))