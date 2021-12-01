from typing import List

def part_one(filename: str) -> int:
    with open(filename) as f:
        depths = list(map(int, f))
    return num_increasing(depths)

def part_two(filename: str) -> int:
    with open(filename) as f:
        depths = list(map(int, f))
    window_depths = [sum([depths[j] for j in range(i, i+3)]) for i in range(len(depths)-2)]
    return num_increasing(window_depths)

def num_increasing(depths: List[str]) -> int:
    return sum([1 if depths[i] > depths[i-1] else 0 for i in range(1, len(depths))])
        
if __name__ == "__main__":
    input_path = "day-01/input.txt"
    print("Part 1")
    print(part_one(input_path))
    print("Part 2")
    print(part_two(input_path))