#!/usr/bin/env python3
from functools import reduce

PAIRS = {'(': ')', '[': ']', '{': '}', '<': '>'}

def part_one(input):
    corrupted = []
    for line in input:
        stack = []
        for c in line:
            if c in PAIRS.keys():
                stack.append(c)
            elif c != PAIRS[stack.pop()]:
                corrupted.append(c)
                break
    return sum(map(lambda c: {')': 3, ']': 57, '}': 1197, '>': 25137}[c], corrupted))

def part_two(input):
    scores = []
    for line in input:
        stack = []
        for c in line:
            if c in PAIRS.keys():
                stack.append(c)
            elif c != PAIRS[stack.pop()]:
                break
        else:
            scores.append(
                reduce(lambda a, b: (5 * a) + {'(': 1, '[': 2, '{': 3, '<': 4}[b], stack[::-1], 0))
    return sorted(scores)[len(scores)//2]

if __name__ == "__main__":
    input_path = "day-10/input.txt"
    with open(input_path) as f:
        input = f.read().splitlines()
    print("Part 1")
    print(part_one(input))
    print("Part 2")
    print(part_two(input))