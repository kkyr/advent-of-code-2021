#!/usr/bin/env python3
import statistics

def part_one(input):
    median = int(statistics.median(input))
    return sum(abs(x - median) for x in input)

def part_two(input):
    avg = int(statistics.mean(input))
    return sum(sum_natural(abs(x - avg)) for x in input)

def sum_natural(n):
    '''Returns the sum of natural numbers up to n'''
    return n * (n + 1) // 2         

if __name__ == "__main__":
    input_path = "day-07/input.txt"
    with open(input_path) as f:
        input = list(map(int, f.readline().strip().split(',')))
    print("Part 1")
    print(part_one(input))
    print("Part 2")
    print(part_two(input))