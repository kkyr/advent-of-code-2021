#!/usr/bin/env python3
def part_one(depths):
    return sum(x < y for x, y in zip(depths, depths[1:]))

def part_two(depths):
    return sum(x < y for x, y in zip(depths, depths[3:]))
        
if __name__ == "__main__":
    input_path = "day-01/input.txt"
    with open(input_path) as f:
        depths = list(map(int, f))
    print("Part 1")
    print(part_one(depths))
    print("Part 2")
    print(part_two(depths))