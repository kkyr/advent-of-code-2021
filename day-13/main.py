#!/usr/bin/env python3
def part_one(dots, folds):
    dots = fold(dots, folds, 1)
    return len(dots)

def part_two(dots, folds):
    dots = fold(dots, folds)
    max_x, max_y = map(max, zip(*dots))
    return "\n".join("".join("#" if (x, y) in dots else "." for x in range(max_x + 1)) for y in range(max_y + 1))

def fold(dots, folds, num_folds=None):
    folds = folds[:num_folds] if num_folds else folds
    fold_by_axis = {
        "x": lambda x, y, fold_val: (x if x <= fold_val else 2 * fold_val - x, y),
        "y": lambda x, y, fold_val: (x, y if y <= fold_val else 2 * fold_val - y)
    }
    for axis, fold_val in folds:
        dots = set(fold_by_axis[axis](x, y, fold_val) for (x, y) in dots)
    return dots

if __name__ == "__main__":
    dots, folds = set(), []
    input_path = "day-13/input.txt"
    for line in open(input_path).read().splitlines():
        if "fold" in line:
            folds.append((line.split("=")[0][-1], int(line.split("=")[1])))
        if "," in line:
            dots.add(tuple(map(int, line.split(","))))
    print("Part 1")
    print(part_one(dots, folds))
    print("Part 2")
    print(part_two(dots, folds))