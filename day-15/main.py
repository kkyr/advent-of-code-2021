#!/usr/bin/env python3
from queue import PriorityQueue
from collections import OrderedDict
from itertools import product

def part_one(grid):
    last = next(reversed(grid))
    D = dijkstra(grid, last[0] + 1)
    return D[last]

def part_two(grid):
    last = next(reversed(grid))
    size = last[0] + 1
    for tile_x in range(5):
        x_start = tile_x * size
        for x in range(x_start, x_start + size):
            if x_start != 0:
                for y in range(size):
                    nv = grid[(x - size, y)] + 1
                    grid[(x, y)] = nv if nv <= 9 else nv - 9
            for tile_y in range(1, 5):
                y_start = tile_y * size
                for y in range(y_start, y_start + size):
                    nv = grid[(x, y - size)] + 1
                    grid[(x, y)] = nv if nv <= 9 else nv - 9

    assert(len(grid) == size * size * 25)
    for x, y in product(range(size), range(size)):
        assert((x, y) in grid)

    return part_one(grid)

def dijkstra(grid, size):
    start = next(iter(grid))
    D = {v: float("inf") for v in grid}
    D[start] = 0

    seen = set()
    pq = PriorityQueue()
    pq.put((0, start))

    while not pq.empty():
        _, cur = pq.get()
        seen.add(cur)
        for av in neighbours(cur, size):
            if av not in seen:
                next_dist = grid[av]
                old_cost = D[av]
                new_cost = D[cur] + next_dist
                if new_cost < old_cost:
                    pq.put((new_cost, av))
                    D[av] = new_cost
    return D

def neighbours(v, length):
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = v[0] + dx, v[1] + dy
        if 0<=nx<length and 0<=ny<length:
            yield (nx, ny)

if __name__ == "__main__":
    input_path = "day-15/input.txt"
    grid = OrderedDict()
    for x, line in enumerate(open(input_path).read().splitlines()):
        for y, num in enumerate(line):
            grid[(x, y)] = int(num)
    print("Part 1")
    print(part_one(grid))
    print("Part 2")
    print(part_two(grid))