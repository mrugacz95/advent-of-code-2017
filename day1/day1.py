from itertools import pairwise

from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=1)


def parse(input_data):
    return list(map(int, list(input_data)))


def part1(input_data):
    data = parse(input_data)
    data = data + [data[0]]
    return sum(map(lambda x: x[0],filter(lambda x: x[0] == x[1], pairwise(data))))


def part2(input_data):
    data = parse(input_data)
    ans = 0
    for i, num in enumerate(data):
       if  data[(i + len(data) // 2) % len(data)] == num:
           ans += num
    return ans


def main():
    assert 3 == part1(puzzle.examples[0].input_data)
    print("part1 example OK")

    puzzle.answer_a = part1(puzzle.input_data)
    print("part1 OK")

    assert 6 == part2('1212')
    print("part2 example OK")

    puzzle.answer_b = part2(puzzle.input_data)
    print("part2 OK")


if __name__ == '__main__':
    main()
