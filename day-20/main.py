#!/usr/bin/env python3
from itertools import chain
from collections import Counter

def part_one(image, algorithm):
    return lit_pixels(enhance(image, algorithm))  

def part_two(image, algorithm):
    return lit_pixels(enhance(image, algorithm, 50)) 

def lit_pixels(image):
    return Counter(chain.from_iterable(image))["#"] 

def enhance(image, algorithm, iterations=2):
    for n in range(iterations):
        fill_char = algorithm[-1] if n % 2 == 0 else algorithm[0]
        image = pad(image, fill_char)
        new_image = [[image[x][y] for y in range(len(image[x]))] for x in range(len(image))]
        for x in range(len(image)):
            for y in range(len(image[x])):
                b = ""
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        nx, ny = x + dx, y + dy
                        if 0<=nx<len(image) and 0<=ny<len(image[y]):
                            b += {".": "0", "#": "1"}[image[nx][ny]]
                        else:
                            b += {".": "0", "#": "1"}[fill_char]
                new_image[x][y] = algorithm[int(b, 2)]
        image = new_image
    return image

def pad(image, fill_char):
    new_size = len(image) + 2
    new_image = [[fill_char] * new_size]
    new_image.extend([[fill_char] + row + [fill_char] for row in image])
    new_image.append([fill_char] * new_size)
    return new_image

if __name__ == "__main__":
    input_path = "day-20/input.txt"
    with open(input_path) as f:
        algorithm, _, *image = f.read().splitlines()
        image = [[px for px in line] for line in image]
    print("Part 1")
    print(part_one(image, algorithm))
    print("Part 2")
    print(part_two(image, algorithm))