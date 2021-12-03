#!/usr/bin/env python3
from collections import Counter

def part_one(rows):
    gamma = n = 0
    bits = len(rows[0])

    for i in range(bits - 1, -1, -1):
        c = Counter(row[i] for row in rows)
        most_common = 0 if c['0'] > c['1'] else 1
        gamma += most_common * 2 ** n
        n += 1

    epsilon = (2 ** bits - 1) - gamma
    return gamma * epsilon

def part_two(rows):
    rows_cpy = rows.copy()
    bits = len(rows[0])

    for i in range(bits):
        c = Counter(row[i] for row in rows)
        most_common = '0' if c['0'] > c['1'] else '1'
        rows = [row for row in rows if row[i] == most_common]
        if len(rows) == 1: break

    for i in range(bits):
        c = Counter(row[i] for row in rows_cpy)
        least_common = '1' if c['1'] < c['0'] else '0'
        rows_cpy = [row for row in rows_cpy if row[i] == least_common]
        if len(rows_cpy) == 1: break

    o2, co2 = int(rows[0], 2), int(rows_cpy[0], 2)
    return o2 * co2

if __name__ == "__main__":
    input_path = "day-03/input.txt"
    with open(input_path) as f:
        rows = f.read().splitlines()
    print("Part 1")
    print(part_one(rows))
    print("Part 2")
    print(part_two(rows))     