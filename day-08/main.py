#!/usr/bin/env python3
from itertools import chain

def part_one(output):
    unique = set([2, 3, 4, 7])
    return sum(len(x) in unique for x in output)

def part_two(signals, output):
    digit_segments = { # encoding a to 0, b to 1, ...
        0: set([0, 1, 2, 4, 5, 6]),
        1: set([2, 5]),
        2: set([0, 2, 3, 4, 6]),
        3: set([0, 2, 3, 5, 6]),
        4: set([1, 2, 3, 5]),
        5: set([0, 1, 3, 5, 6]),
        6: set([0, 1, 3, 4, 5, 6]),
        7: set([0, 2, 5]),
        8: set([0, 1, 2, 3, 4, 5, 6]),
        9: set([0, 1, 2, 3, 5, 6])
    }
    total_sum = 0
    for idx, signal in enumerate(signals):
        assert(len(signal) == 10)
        signal = sorted(signal, key=len)

        decoded_segments = {}
        one, four, seven = set(signal.pop(0)), set(signal.pop(1)), set(signal.pop(0)) # deduced due to unique lengths

        seg_0 = seven.difference(one)
        decoded_segments[list(seg_0).pop()] = 0

        for i in range(3):
            if seven.issubset(signal[i]):
                three = set(signal.pop(i))
                break

        seg_3 = four.intersection(three).difference(one)
        decoded_segments[list(seg_3).pop()] = 3

        seg_1 = four.difference(one).difference(seg_3)
        decoded_segments[list(seg_1).pop()] = 1

        seg_6 = three.difference(one).difference(set(decoded_segments.keys()))
        decoded_segments[list(seg_6).pop()] = 6

        for i in range(2):
            if set(decoded_segments.keys()).issubset(signal[i]):
                five = set(signal.pop(i))
                break
        
        seg_5 = five.difference(decoded_segments.keys())
        decoded_segments[list(seg_5).pop()] = 5

        seg_2 = one.difference(seg_5)
        decoded_segments[list(seg_2).pop()] = 2

        two = set(signal.pop(0)) # last len==5 element
        
        seg_4 = two.difference(decoded_segments.keys())
        decoded_segments[list(seg_4).pop()] = 4

        out_decoded = [list(map(lambda seg: decoded_segments[seg], out)) for out in output[idx]]

        sum = 0
        for d in out_decoded:
            for digit, segment in digit_segments.items():
                if set(d) == segment:
                    sum = sum * 10 + digit
                    break
        total_sum += sum

    return total_sum

if __name__ == "__main__":
    input_path = "day-08/input.txt"
    with open(input_path) as f:
        input = [line.strip().split(' | ') for line in f.readlines()]
        signals = [line[0].split(' ') for line in input]
        output = [line[1].split(' ') for line in input]
    print("Part 1")
    print(part_one(chain.from_iterable(output)))
    print("Part 2")
    print(part_two(signals, output))