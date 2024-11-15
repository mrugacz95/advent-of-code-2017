import unittest
from functools import cache
from typing import List, Tuple

from aocd.models import Puzzle
from matplotlib.style.core import available
from tqdm import tqdm

puzzle = Puzzle(year=2017, day=16)


def parse(input_data):
    moves = []
    for move in input_data.split(","):
        symbol = move[0]
        if symbol == "s":
            a = int(move[1:])
            assert 0 <= a < 16
            data = (a,)
        elif symbol == "x":
            a, b = move[1:].split("/")
            a, b = int(a), int(b)
            assert 0 <= a < 16
            assert 0 <= b < 16
            data = (a, b)
        elif symbol == "p":
            a, b = move[1:].split("/")
            assert ord('a') <= ord(a) <= ord('p')
            assert ord('a') <= ord(b) <= ord('p')
            data = (a, b)
        else:
            raise ValueError(f"Unexpected symbol {symbol}")
        moves.append((symbol, data))
    return moves


def spin(programs, num):
    return programs[-num:] + programs[:len(programs) - num]


def exchange(programs, a, b):
    programs[a], programs[b] = programs[b], programs[a]
    return programs


def partner(programs: List[str], a, b):
    idx_a = programs.index(a)
    idx_b = programs.index(b)
    programs[idx_a], programs[idx_b] = programs[idx_b], programs[idx_a]
    return programs


def part1(count, input_data):
    data = parse(input_data)
    programs = [chr(ord('a') + i) for i in range(count)]
    for op, params in data:
        programs = {
            's': spin,
            'x': exchange,
            'p': partner,
        }.get(op)(programs, *params)
    return ''.join(programs)


def part2(count, input_data, repeats):
    data = parse(input_data)
    programs = [chr(ord('a') + i) for i in range(count)]

    def full_dance(operations, permutation):
        for op, params in operations:
            permutation = {
                's': spin,
                'x': exchange,
                'p': partner,
            }.get(op)(list(permutation), *params)
        return ''.join(permutation)

    cache = {}
    programs = ''.join(programs)
    i = 0
    progress = tqdm()
    while i < repeats:
        progress.update()
        if programs in cache:
            cycle_start = cache[programs][0]
            cycle_end = i
            cycle_length = cycle_end - cycle_start
            available = (repeats - cycle_length) // cycle_length
            i += cycle_length * available
            break
        cache[programs] = (i, programs)
        programs = full_dance(data, programs)
        i += 1

    while i < repeats:
        programs = cache[programs][1]
        i += 1

    return ''.join(programs)


class Day16(unittest.TestCase):

    def test_example(self):
        programs = list("abcde")
        programs = spin(programs, 5)
        self.assertEqual(programs, ['a', 'b', 'c', 'd', 'e'])
        programs = exchange(programs, 0, 4)
        self.assertEqual(programs, ['e', 'b', 'c', 'd', 'a'])
        programs = partner(programs, 'a', 'e')
        self.assertEqual(programs, ['a', 'b', 'c', 'd', 'e'])
        programs = part1(16, "x14/15")
        self.assertEqual(programs[-3:], "npo")
        programs = part1(16, "x0/1")
        self.assertEqual(programs[:3], "bac")
        programs = part1(16, "pa/a")
        self.assertEqual(programs[:3], "abc")
        programs = part1(16, "s10")
        self.assertEqual(programs, "ghijklmnopabcdef")

    def test_part1_example(self):
        self.assertEqual("baedc", part1(5, puzzle.examples[0].input_data))

    def test_part1(self):
        puzzle.answer_a = part1(16, puzzle.input_data)
        self.assertTrue(puzzle.answered_a)

    def test_input(self):
        with open("input.txt", "r") as puzzle_input:
            result = part2(16, puzzle_input.read(), 1000000000)
            print("Part 1:", result)

    def test_part2_example(self):
        self.assertEqual("ceadb", part2(5, puzzle.examples[0].input_data, 2))

    def test_part2(self):
        puzzle.answer_b = part2(16, puzzle.input_data, 1000000000)
        self.assertTrue(puzzle.answered_b)


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Day16)
    unittest.TextTestRunner().run(suite)
