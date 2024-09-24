import sys

from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=11)


def parse(input_data):
    return input_data.split(",")


directions = {
    'n': (0, -1, 1),
    's': (0, 1, -1),
    'ne': (1, -1, 0),
    'sw': (-1, 1, 0),
    'nw': (-1, 0, +1),
    'se': (1, 0, -1),
}


def part1(input_data):
    data = parse(input_data)
    x, y, z = (0, 0, 0)
    for step in data:
        dy, dx, dz = directions.get(step)
        x, y, z = x + dx, y + dy, z + dz
    return (abs(x) + abs(y) + abs(z)) // 2


def part2(input_data):
    data = parse(input_data)
    x, y, z = (0, 0, 0)
    furthest = -sys.maxsize - 1
    for step in data:
        dy, dx, dz = directions.get(step)
        x, y, z = x + dx, y + dy, z + dz
        furthest = max(furthest, (abs(x) + abs(y) + abs(z)) // 2)
    return furthest


def main():
    assert 3 == part1("ne,ne,ne")
    assert 0 == part1("ne,ne,sw,sw")
    assert 2 == part1("ne,ne,s,s")
    assert 3 == part1("se,sw,se,sw,sw")
    print("part1 example OK")

    puzzle.answer_a = part1(puzzle.input_data)
    print("part1 OK")

    puzzle.answer_b = part2(puzzle.input_data)
    print("part2 OK")


if __name__ == '__main__':
    main()
