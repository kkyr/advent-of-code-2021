#!/usr/bin/env python3
from enum import Enum
from functools import reduce
from operator import *

class Operator(Enum):
    SUM = 0
    PRODUCT = 1
    MIN = 2
    MAX = 3
    GT = 5
    LT = 6
    EQ = 7

def solve(hex):
    b = (bin(int(hex, 16))[2:]).zfill(len(hex) * 4)
    versions = 0

    def parse_expression(i):
        nonlocal versions
        version = int(b[i:i+3], 2)
        i += 3
        versions += version

        packet_type = int(b[i:i+3], 2)
        i += 3

        # LITERAL VALUE PACKET
        if packet_type == 4:
            res = ""
            while i + 5 <= len(b):
                res += b[i+1:i+5]
                i += 5
                if b[i-5] == "0":
                    break
            return i, int(res, 2)

        # OPERATOR PACKET
        length_type = int(b[i], 2)
        i += 1
        res = 0
        operands = []
        if length_type == 0:
            sub_packets_bits = int(b[i:i+15], 2)
            i += 15
            max_bit = i + sub_packets_bits
            while i < max_bit:
                i, op = parse_expression(i)
                operands.append(op)
        else:
            sub_packets_num = int(b[i:i+11], 2)
            i += 11
            for _ in range(sub_packets_num):
                i, op = parse_expression(i)
                operands.append(op)

        match Operator(packet_type):
            case Operator.SUM: res = sum(operands)
            case Operator.PRODUCT: res = reduce(mul, operands, 1)
            case Operator.MIN: res = min(operands)
            case Operator.MAX: res = max(operands)
            case Operator.GT: res = gt(*operands)
            case Operator.LT: res = lt(*operands)
            case Operator.EQ: res = eq(*operands)
            case _: assert False, f"unknown packet type {packet_type}"

        return i, res

    _, res = parse_expression(0)
    print("Part 1")
    print(versions)
    print("Part 2")
    print(res)

if __name__ == "__main__":
    input_path = "day-16/input.txt"
    with open(input_path) as f:
        input = f.readline()
    solve(input)