import re

from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=2)


def parse(input_data):
    lines = input_data.split("\n")
    data = []
    for line in lines:
        numbers = list(map(int, re.split("[\t ]", line)))
        data.append(numbers)
    return data


def part1(input_data):
    data = parse(input_data)
    diff = []
    for numbers in data:
        s = sorted(numbers)
        diff.append(s[-1] - s[0])
    return sum(diff)


def part2(input_data):
    data = parse(input_data)
    ans = 0
    for numbers in data:
        def find_divisible():
            s = sorted(numbers)
            for i in range(len(s)):
                for j in range(i + 1, len(s)):
                    if s[j] % s[i] == 0:
                        return s[j] // s[i]
            raise RuntimeError("No divisible numbers found")

        ans += find_divisible()
    return ans


def main():
    assert 18 == part1(puzzle.examples[0].input_data)
    print("part1 example OK")

    puzzle.answer_a = part1(puzzle.input_data)
    print("part1 OK")

    assert 9 == part2(("5 9 2 8\n"
                       "9 4 7 3\n"
                       "3 8 6 5"))
    print("part2 example OK")

    puzzle.answer_b = part2(puzzle.input_data)
    print("part2 OK")


if __name__ == '__main__':
    main()
