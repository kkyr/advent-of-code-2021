#!/usr/bin/env python3
from collections import defaultdict

def polymerize(polymer, rules, steps):
    pair_cnt = defaultdict(int)
    for i in range(len(polymer) - 1):
        pair_cnt[polymer[i:i+2]] += 1

    for _ in range(steps):
        new_pair_cnt = defaultdict(int)
        for pair, cnt in pair_cnt.items():
            assert(pair in rules)
            new_pair_cnt[pair[0] + rules[pair]] += cnt
            new_pair_cnt[rules[pair] + pair[1]] += cnt
        pair_cnt = new_pair_cnt
    
    letter_cnt = defaultdict(int)
    for pair, cnt in pair_cnt.items():
        letter_cnt[pair[0]] += cnt
    letter_cnt[polymer[-1]] += 1
    return max(letter_cnt.values()) - min(letter_cnt.values())

if __name__ == "__main__":
    input_path = "day-14/input.txt"
    with open(input_path) as f:
        polymer = f.readline().strip()
        rules = dict([l.split(" -> ") for l in f.read().splitlines() if l])
    print("Part 1")
    print(polymerize(polymer, rules, 10))
    print("Part 2")
    print(polymerize(polymer, rules, 40))