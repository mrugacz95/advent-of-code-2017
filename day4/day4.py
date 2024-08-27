from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=4)


def parse(input_data):
    return input_data.split("\n")


def part1(input_data):
    data = parse(input_data)
    valid = 0
    for line in data:
        passwords = line.split(" ")
        if len(set(passwords)) == len(passwords):
            valid += 1
    return valid


def part2(input_data):
    data = parse(input_data)
    valid = 0
    for line in data:
        passwords = list(map(lambda s: ''.join(sorted(s)), line.split(' ')))
        if len(set(passwords)) == len(passwords):
            valid += 1
    return valid

def main():
    assert 1 == part1(puzzle.examples[0].input_data)
    print("part1 example OK")

    puzzle.answer_a = part1(puzzle.input_data)
    print("part1 OK")

    assert 1 == part2('abcde fghij\nabcde xyz ecdab\noiii ioii iioi iiio')
    print("part2 example OK")

    puzzle.answer_b = part2(puzzle.input_data)
    print("part2 OK")


if __name__ == '__main__':
    main()
