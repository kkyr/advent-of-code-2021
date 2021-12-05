#!/usr/bin/env python3
import re
from itertools import filterfalse
from collections import defaultdict, namedtuple
from typing import List

def part_one(lines):
    lines = filterfalse(lambda l: not l.is_horizontal() and not l.is_vertical(), lines)
    dd = defaultdict(int)
    for line in lines:
        for c in line.coords(): 
            dd[c] += 1
    return len(list(v for v in dd.values() if v > 1))

def part_two(lines):
    lines = filterfalse(lambda l: not l.is_horizontal() and not l.is_vertical() and not l.is_diagonal(), lines)
    dd = defaultdict(int)
    for line in lines:
        for c in line.coords(): 
            dd[c] += 1
    return len(list(v for v in dd.values() if v > 1))

class Line:
    class Coordinate(namedtuple('Coordinate', ['x', 'y'])):
        pass

    def __init__(self, start: Coordinate, end: Coordinate):
        self._start = start
        self._end = end 

    def is_vertical(self) -> bool:
        return self._start.x == self._end.x

    def is_horizontal(self) -> bool:
        return self._start.y == self._end.y
    
    def is_diagonal(self) -> bool:
        return abs(self._start.x - self._end.x) == abs(self._start.y - self._end.y)

    def coords(self) -> List[Coordinate]:
        assert(self.is_horizontal() or self.is_vertical() or self.is_diagonal())
        if self.is_horizontal():
            return ((x, self._start.y) for x in range_abs(self._start.x, self._end.x))
        elif self.is_vertical():
            return ((self._start.x, y) for y in range_abs(self._start.y, self._end.y))
        else:
            return zip((x for x in range_abs(self._start.x, self._end.x)), (y for y in range_abs(self._start.y, self._end.y)))

def range_abs(start, stop):
    return range(start, stop + 1) if start < stop else range(start, stop - 1, -1)

if __name__ == "__main__":
    input_path = "day-05/input.txt"
    with open(input_path) as f:
        lines = []
        for line in f:
            x1, y1, x2, y2 = re.findall(r'(\d+)', line)
            lines.append(Line(Line.Coordinate(int(x1), int(y1)), Line.Coordinate(int(x2), int(y2))))
    print("Part 1")
    print(part_one(lines))
    print("Part 2")
    print(part_two(lines))