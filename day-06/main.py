#!/usr/bin/env python3
from collections import Counter

def part_one(fish):
    return solve(fish, 80)  

def part_two(fish):
    return solve(fish, 256)

def solve(fish, days):
    fish_age = Counter(fish)
    for _ in range(days):
        new_fish = fish_age[0]
        for i in range(8):
            fish_age[i] = fish_age[i+1]
        fish_age[6] += new_fish
        fish_age[8] = new_fish
    return sum(fish_age.values())

if __name__ == "__main__":
    input_path = "day-06/input.txt"
    with open(input_path) as f:
        fish = list(map(int, f.readline().split(",")))
    print("Part 1")
    print(part_one(fish))
    print("Part 2")
    print(part_two(fish))