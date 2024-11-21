import numbers
import unittest
from typing import Optional

from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=17)


def parse(input_data):
    return int(input_data)


def part1(input_data):
    steps = parse(input_data)
    numbers = [0]
    pos = 0
    for i in range(2017):
        pos = (pos + steps) % len(numbers) + 1
        numbers.insert(pos, i + 1)
    return numbers[pos + 1]


def part2(input_data, insertions):
    steps = parse(input_data)
    length = 1
    pos = 0
    zero_pos = 0
    answer : Optional[int] = None
    for i in range(insertions):
        pos = (pos + steps) % length + 1
        if pos == zero_pos + 1:
            answer = i + 1
        elif pos < zero_pos:
            zero_pos += 1
        length += 1
    return answer


class Day17(unittest.TestCase):

    def test_part1_example(self):
        self.assertEqual(638, part1(puzzle.examples[0].input_data))

    def test_part1(self):
        puzzle.answer_a = part1(puzzle.input_data)

    def test_part2_example(self):
        self.assertEqual(9, part2(puzzle.examples[0].input_data, 9))

    def test_part2(self):
        puzzle.answer_b = part2(puzzle.input_data, 50000000)


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Day17)
    unittest.TextTestRunner().run(suite)
