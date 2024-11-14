import re
import unittest

from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=15)


def parse(input_data):
    groups = re.match("Generator A starts with (\d+)\nGenerator B starts with (\d+)", input_data).groups()
    return int(groups[0]), int(groups[1])


def generator(initial, factor):
    value = initial
    while True:
        value = (value * factor) % 2147483647
        yield value


def part1(input_data):
    initial_a, initial_b = parse(input_data)
    gen_a = generator(initial_a, 16807)
    gen_b = generator(initial_b, 48271)
    counter = 0
    mask = (1 << 16) - 1
    for _ in range(40_000_000):
        val_a, val_b = next(gen_a), next(gen_b)
        if val_a & mask == val_b & mask:
            counter += 1
    return counter


def part2(input_data):
    initial_a, initial_b = parse(input_data)
    gen_a = generator(initial_a, 16807)
    gen_b = generator(initial_b, 48271)
    counter = 0
    mask = (1 << 16) - 1
    for _ in range(5_000_000):
        val_a = next(a for a in gen_a if a & 3 == 0)
        val_b = next(b for b in gen_b if b & 7 == 0 )
        if val_a & mask == val_b & mask:
            counter += 1
    return counter


class Day15(unittest.TestCase):

    def test_part1_example(self):
        self.assertEqual(588, part1(puzzle.examples[0].input_data))

    def test_part1(self):
        puzzle.answer_a = part1(puzzle.input_data)

    def test_part2(self):
        self.assertEqual(309, part2(puzzle.examples[0].input_data))

    def test_part2_example(self):
        puzzle.answer_b = part2(puzzle.input_data)


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Day15)
    unittest.TextTestRunner().run(suite)
