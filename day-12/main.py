#!/usr/bin/env python3
from collections import defaultdict
from functools import cache

@cache
def count_paths(v, seen, twice_allowed):
    if v == "end": 
        return 1
    paths = 0
    for nv in edges[v]:
        if nv[0].isupper():
            paths += count_paths(nv, seen, twice_allowed)
        elif nv not in seen:
            paths += count_paths(nv, seen | {nv}, twice_allowed)
        elif nv not in {"start", "end"} and twice_allowed:
            paths += count_paths(nv, seen | {nv}, False)
    return paths

if __name__ == "__main__":
    input_path = "day-12/input.txt"
    edges = defaultdict(list)
    for line in open(input_path):
        v, nv = line.strip().split("-")
        edges[v].append(nv)
        edges[nv].append(v)
    print("Part 1")
    print(count_paths("start", frozenset({"start"}), False))
    print("Part 2")
    print(count_paths("start", frozenset({"start"}), True))