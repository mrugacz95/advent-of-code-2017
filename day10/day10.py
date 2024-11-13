from functools import reduce
from itertools import batched

from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=10)


def parse_part1(input_data):
    return list(map(int, input_data.split(",")))


def twist_sequence(sequence, lengths):
    result = sequence.copy()
    pos = 0
    skip_size = 0
    for length in lengths:
        for offset in range(length // 2):
            i, j = (pos + offset) % len(result), (pos + length - offset - 1) % len(result)
            result[i], result[j] = result[j], result[i]
        pos += length + skip_size
        skip_size += 1
    return result


def part1(sequence, input_data):
    lengths = parse_part1(input_data)
    hashed = twist_sequence(sequence, lengths)
    return hashed[0] * hashed[1]


def parse_part2(input_data):
    return list(map(ord, ''.join(input_data.split(", "))))


def full_twist_sequence(pos, skip_size, sequence, lengths):
    result = sequence.copy()
    for length in lengths:
        for offset in range(length // 2):
            i, j = (pos + offset) % len(result), (pos + length - offset - 1) % len(result)
            result[i], result[j] = result[j], result[i]
        pos += length + skip_size
        skip_size += 1
    return result, pos, skip_size


def to_dense_hash(sequence):
    result = []
    for seq in batched(sequence, 16):
        result.append(reduce(lambda a, b: a ^ b, seq))
    return result


def to_hex(sequence):
    result = ''
    for i in sequence:
        result += f'{i:02x}'
    return result


def knot_hash(data):
    lengths = parse_part2(data) + [17, 31, 73, 47, 23]
    sequence = list(range(256))
    pos, skip_size = 0, 0
    for i in range(64):
        sequence, pos, skip_size = full_twist_sequence(pos, skip_size, sequence, lengths)
    sequence = to_dense_hash(sequence)
    hexed = to_hex(sequence)
    return hexed


def part2(input_data):
    return knot_hash(input_data)


def main():
    assert 12 == part1(list(range(5)), puzzle.examples[0].input_data)
    print("part1 example OK")

    puzzle.answer_a = part1(list(range(256)), puzzle.input_data)
    print("part1 OK")

    assert 'a2582a3a0e66e6e86e3812dcb672a272' == part2('')
    assert '33efeb34ea91902bb2f59c9920caa6cd' == part2('AoC 2017')
    assert '3efbe78a8d82f29979031a4aa0b16a9d' == part2('1,2,3')
    assert '63960835bcdc130f0b66d7ff4f6a5a8e' == part2('1,2,4')
    print("part2 example OK")

    puzzle.answer_b = part2(puzzle.input_data)
    print("part2 OK")


if __name__ == '__main__':
    main()
