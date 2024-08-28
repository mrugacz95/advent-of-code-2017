import re

import numpy as np
from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=6)


def parse(input_data):
    return list(map(int,re.split(r"[ \t]", input_data)))


def part1(input_data):
    data = parse(input_data)
    def choose_bank():
        return np.argmax(data)
    def distribute(bank_id):
        blocks = data[bank_id]
        data[bank_id] = 0
        offset = 1
        while blocks > 0:
            data[(bank_id + offset) % len(data)] += 1
            blocks -= 1
            offset += 1
    seen = set()
    seen.add(tuple(data))
    cycles = 0
    while True:
        cycles += 1
        bank_id = choose_bank()
        distribute(bank_id)
        if tuple(data) in seen:
            break
        seen.add(tuple(data))
    return cycles



def part2(input_data):
    data = parse(input_data)
    def choose_bank():
        return np.argmax(data)
    def distribute(bank_id):
        blocks = data[bank_id]
        data[bank_id] = 0
        offset = 1
        while blocks > 0:
            data[(bank_id + offset) % len(data)] += 1
            blocks -= 1
            offset += 1
    seen = {tuple(data): 0}
    cycles = 0
    while True:
        cycles += 1
        bank_id = choose_bank()
        distribute(bank_id)
        if tuple(data) in seen:
            return cycles - seen[tuple(data)]
        seen[tuple(data)]= cycles


def main():
    assert 5 == part1(puzzle.examples[0].input_data)
    print("part1 example OK")

    puzzle.answer_a = part1(puzzle.input_data)
    print("part1 OK")

    assert 4 == part2(puzzle.examples[0].input_data)
    print("part2 example OK")

    puzzle.answer_b = part2(puzzle.input_data)
    print("part2 OK")


if __name__ == '__main__':
    main()
