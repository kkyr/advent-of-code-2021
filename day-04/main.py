#!/usr/bin/env python3
from itertools import chain, filterfalse

NUMBER_SEEN_FLAG = -1

def part_one(winning_nums, boards):
    for num in winning_nums:
        for board in boards:
            mark_board(board, num)
            if board_won(board):
                return num * sum_unseen(board)

def part_two(winning_nums, boards):
    for num in winning_nums:
        i, n = 0, len(boards)
        while i < n:
            mark_board(boards[i], num)
            if board_won(boards[i]):
                winning_board = (num, boards[i])
                del boards[i]
                n -= 1
            else:
                i += 1
    return winning_board[0] * sum_unseen(winning_board[1])

def mark_board(board, num):
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == num:
                board[y][x] = NUMBER_SEEN_FLAG

def board_won(board):
    winning_line = lambda line: all(x == NUMBER_SEEN_FLAG for x in line)
    get_column = lambda matrix, i: [row[i] for row in matrix]
    return any(winning_line(board[i]) or winning_line(get_column(board, i)) for i in range(len(board)))

def sum_unseen(board):
    return sum(filterfalse(lambda x: x == NUMBER_SEEN_FLAG, chain.from_iterable(board)))

def grouper(input, n):
    iters = [iter(input)] * n
    return list(zip(*iters))

if __name__ == "__main__":
    with open("day-04/input.txt") as f:
        winning_nums = list(map(int, f.readline().split(',')))
        rows = [[int(x) for x in row.strip().split(' ') if x.isdigit()] for row in f if row != '\n']
        boards = grouper(rows, 5)

    print("Part 1")
    print(part_one(winning_nums, boards))
    print("Part 2")
    print(part_two(winning_nums, boards))   