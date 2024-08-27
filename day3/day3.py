from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=3)


def parse(input_data):
    return int(input_data)

next_dir = {
    'r': 'u',
    'u': 'l',
    'l': 'd',
    'd': 'r',
}
delta = {
    'r': (0, 1),
    'u': (1, 0),
    'l': (0, -1),
    'd': (-1, 0),
}
len_increase = {
    'r': 1,
    'l': 1,
    'u': 0,
    'd': 0,
}
anticlockwise = {
    'r': 'u',
    'u': 'l',
    'l': 'd',
    'd': 'r'
}

def part1(input_data):
    target = parse(input_data)
    length = 0
    pos = (0, 0)
    id = 1
    direction = 'r'
    while id < target:
        length += len_increase[direction]
        id += length
        y, x = delta[direction]
        pos = pos[0] + x * length, pos[1] + y * length
        direction = next_dir[direction]
    if id != target:
        before = anticlockwise[direction]
        y, x = delta[before]
        diff = id - target
        pos = pos[0] + x * diff, pos[1] + y * diff
    dist = abs(pos[0]) + abs(pos[1])
    return dist


def part2(input_data):
    target = parse(input_data)
    spiral = {
        (0, 0): 1
    }
    neighbours = [
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
    ]
    direction = 'r'
    length = 1
    pos = (0, 0)
    while True:
        for _ in range(length):
            y,x = delta[direction]
            pos = pos[0] + y, pos[1] + x
            neighbours_sum = 0
            for ny,nx in neighbours:
                n = pos[0] + ny, pos[1] + nx
                value = spiral.get(n, 0)
                neighbours_sum += value
            spiral[pos] = neighbours_sum
            if spiral[pos] > target:
                return spiral[pos]
        direction = next_dir[direction]
        length += len_increase[direction]


def main():
    for idx, example in enumerate(puzzle.examples):
        assert int(example.answer_a) == part1(example.input_data)
        print(f"part1 example {idx} OK")

    puzzle.answer_a = part1(puzzle.input_data)
    print("part1 OK")

    assert 806 == part2(750)
    print("part2 example OK")

    puzzle.answer_b = part2(puzzle.input_data)
    print("part2 OK")


if __name__ == '__main__':
    main()
