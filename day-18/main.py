#!/usr/bin/env python3
import math
import functools
from itertools import permutations

EXPLODE_DEPTH = 5
SPLIT_THRESHOLD = 10

def parse(raw_snail):
    depths, values = [], []
    cur_depth = 0
    for ch in raw_snail:
        if ch == '[': cur_depth += 1
        elif ch == ']': cur_depth -= 1
        elif ch in '1234567890': values.append(int(ch))
        elif ch == ',': depths.append(cur_depth)
    return (depths, values)

def explode(snail):
    depths, values = snail
    if EXPLODE_DEPTH not in depths:
        return snail, False

    i = depths.index(EXPLODE_DEPTH)
    new_values = values.copy()
    if i > 0:
        new_values[i-1] += values[i]
    if i+2 < len(new_values):
        new_values[i+2] += values[i+1]
    return (depths[:i] + depths[i+1:], new_values[:i] + [0] + new_values[i+2:]), True

def split(snail):
    depths, values = snail
    v = next((v for v in values if v >= SPLIT_THRESHOLD), None)
    if not v:
        return snail, False

    i = values.index(v)
    new_depth = 1 + max(depths[i-1] if i > 0 else 0, depths[i] if i < len(depths) else 0)
    new_values = values[:i] + [v//2, math.ceil(v/2)] + values[i+1:]
    return (depths[:i] + [new_depth] + depths[i:], new_values), True

def reduce(snail):
    while True:
        snail, ok = explode(snail)
        if ok: continue
        snail, ok = split(snail)
        if not ok: break
    return snail

def add(snail_1, snail_2):
    depths_1, values_1 = snail_1
    depths_2, values_2 = snail_2
    return reduce(
        ([d+1 for d in depths_1] + [1] + [d+1 for d in depths_2], values_1 + values_2))

def magnitude(snail):
    depths, values = snail
    while True:
        if not depths: break
        i = depths.index(max(depths))
        values[i] = values[i] * 3 + values[i+1] * 2
        del values[i+1]
        del depths[i]
    assert len(values) == 1
    return values[0]

def part_one(snails):
    return magnitude(functools.reduce(add, snails))

def part_two(snails):
    return max(
        magnitude(functools.reduce(add, perm)) for perm in permutations(snails, 2)
    )

if __name__ == "__main__":
    input_path = "day-18/input.txt"
    with open(input_path) as f:
        snails = [parse(l) for l in f.read().splitlines()]
    print("Part 1")
    print(part_one(snails))
    print("Part 2")
    print(part_two(snails))