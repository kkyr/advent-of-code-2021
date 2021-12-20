#!/usr/bin/env python3
from itertools import chain, combinations

def solve(scanners):
    aligned = [scanners.pop(0)]
    scanner_pos = [(0, 0, 0)]
    while scanners:
        s1 = scanners.pop(0)
        for s0 in aligned:
            alignment = try_align(s0, s1)
            if alignment:
                (d1, r1, dist), (d2, r2, ddist), (d3, r3, dddist) = alignment
                aligned.append(list(
                    (b[d1] * r1 - dist, b[d2] * r2 - ddist, b[d3] * r3 - dddist)
                    for b in s1
                ))
                scanner_pos.append((dist, ddist, dddist))
                break
        else:
            scanners.append(s1)

    print("Part 1")
    print(len(set(chain.from_iterable(aligned))))
    
    max_dist = 0
    for c in combinations(scanner_pos, 2):
        max_dist = max(max_dist, sum([
            c[0][0] - c[1][0],
            c[0][1] - c[1][1],
            c[0][2] - c[1][2]
        ]))
    print("Part 2")
    print(max_dist)

def try_align(aligned, candidate):
    for b1 in candidate:
        for b0 in aligned:
            for dim in range(3):
                for r in [1, -1]:
                    c = r*b1[dim]
                    dist = c - b0[0]
                    count = 0
                    for bb1 in candidate:
                        for bb0 in aligned:
                            if (r * bb1[dim] - dist) == bb0[0]:
                                count += 1
                    if count >= 12:
                        for ddim in range(3):
                            if ddim != dim:
                                for rr in [1, -1]:
                                    c = rr*b1[ddim]
                                    ddist = c - b0[1]
                                    count = 0
                                    for bb1 in candidate:
                                        for bb0 in aligned:
                                            if (rr * bb1[ddim] - ddist) == bb0[1]:
                                                count += 1
                                    if count >= 12:
                                         for dddim in range(3):
                                            if dddim != ddim and dddim != dim:
                                                for rrr in [1, -1]:
                                                    c = rrr*b1[dddim]
                                                    dddist = c - b0[2]
                                                    count = 0
                                                    for bb1 in candidate:
                                                        for bb0 in aligned:
                                                            if (rrr * bb1[dddim] - dddist) == bb0[2]:
                                                                count += 1
                                                    if count >= 12:
                                                        return (dim, r, dist), (ddim, rr, ddist), (dddim, rrr, dddist)

if __name__ == "__main__":
    input_path = "day-19/input.txt"
    scanners = []
    for l in open(input_path).read().splitlines():
        if "scanner" in l:
            scanners.append([])
        elif l:
            scanners[-1].append(tuple(map(int, l.split(","))))
    print("Part 1")
    solve(scanners)