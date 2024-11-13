import unittest

from aocd.models import Puzzle

from day10.day10 import knot_hash


def parse(input_data):
    return input_data


def str_to_bin(data):
    def char_to_bin(c: str) -> str:
        if c.isdigit():
            num = ord(c) - ord('0')
        else:
            num = ord(c) - ord('a') + 10
        return f"{num:04b}"

    return ''.join(char_to_bin(c) for c in data)


def part1(input_data):
    data = parse(input_data)
    ans = 0
    for row in range(128):
        hashed = knot_hash(f"{data}-{row}")
        bin = str_to_bin(hashed)
        ones = len(list(filter(lambda x: x == '1', bin)))
        ans += ones
    return ans


def part2(input_data):
    data = parse(input_data)
    ans = 0
    matrix = []
    for row in range(128):
        hashed = knot_hash(f"{data}-{row}")
        bin = str_to_bin(hashed)
        matrix.append(list(bin))
    neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = set()

    def flood(y, x):
        if y < 0 or y >= len(matrix) or x < 0 or x >= len(matrix[0]):
            return 0
        if (y, x) in visited:
            return 0
        visited.add((y, x))
        if matrix[y][x] == '0':
            return 0
        sum = 0
        for ny, nx in neighbours:
            sum += flood(ny + y, nx + x)
        sum += 1
        return sum

    groups = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            group_size = flood(y, x)
            if group_size > 0:
                groups += 1
    return groups


class Day14(unittest.TestCase):
    puzzle = Puzzle(year=2017, day=14)

    def test_part1_example(self):
        self.assertEqual(8108, part1(self.puzzle.examples[0].input_data))

    def test_part1(self):
        self.puzzle.answer_a = part1(self.puzzle.input_data)

    def test_part2(self):
        self.assertEqual(1242, part2(self.puzzle.examples[0].input_data))

    def test_part2_example(self):
        self.puzzle.answer_b = part2(self.puzzle.input_data)


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(Day14)
    unittest.TextTestRunner().run(suite)
