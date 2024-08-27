from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=5)


def parse(input_data):
    return list(map(int,input_data.split("\n")))


def part1(input_data):
    data = parse(input_data)
    pointer = 0
    steps = 0
    while True:
        steps += 1
        inc = pointer
        pointer += data[pointer]
        if 0 <= pointer < len(data):
            data[inc] += 1
        else:
            break
    return steps


def part2(input_data):
    data = parse(input_data)
    pointer = 0
    steps = 0
    while True:
        steps += 1
        inc = pointer
        offset = data[pointer]
        pointer += offset
        if 0 <= pointer < len(data):
            if offset >= 3:
                data[inc] -= 1
            else:
                data[inc] += 1
        else:
            break
    return steps


def main():
    assert 5 == part1(puzzle.examples[0].input_data)
    print("part1 example OK")

    puzzle.answer_a = part1(puzzle.input_data)
    print("part1 OK")

    assert 10 == part2(puzzle.examples[0].input_data)
    print("part2 example OK")

    puzzle.answer_b = part2(puzzle.input_data)
    print("part2 OK")


if __name__ == '__main__':
    main()
