#!/usr/bin/env python3
from itertools import product

def part_one(G):
    R = len(G)
    C = len(G[0])

    def flash(G, r, c, flashed):
        flashed.add((r, c))
        G[r][c] = 0
        flashes = 1
        for dr, dc in product([-1, 0, 1], [-1, 0, 1]):
            rr = r + dr
            cc = c + dc
            if 0<=rr<R and 0<=cc<C and (rr, cc) not in flashed:
                G[rr][cc] += 1
                if G[rr][cc] == 10:
                    flashes += flash(G, rr, cc, flashed)
        return flashes

    flashes = 0
    for _ in range(100):
        flashed = set()
        for r in range(R):
            for c in range(C):
                if (r, c) not in flashed:
                    G[r][c] += 1
                    if G[r][c] == 10:
                        flashes += flash(G, r, c, flashed)
    return flashes


def part_two(G):
    R = len(G)
    C = len(G[0])

    def flash(G, r, c, flashed):
        flashed.add((r, c))
        G[r][c] = 0
        for dr, dc in product([-1, 0, 1], [-1, 0, 1]):
            rr = r + dr
            cc = c + dc
            if 0<=rr<R and 0<=cc<C and (rr, cc) not in flashed:
                G[rr][cc] += 1
                if G[rr][cc] == 10:
                    flash(G, rr, cc, flashed)

    step = 0
    while True:
        flashed = set()
        step += 1
        for r in range(R):
            for c in range(C):
                if (r, c) not in flashed:
                    G[r][c] += 1
                    if G[r][c] == 10:
                        flash(G, r, c, flashed)
        if len(flashed) == C * R:
            return step

if __name__ == "__main__":
    input_path = "day-11/input.txt"
    with open(input_path) as f:
        input = [[int(x) for x in line] for line in f.read().splitlines()]
    print("Part 1")
    print(part_one([r[:] for r in input]))
    print("Part 2")
    print(part_two(input))