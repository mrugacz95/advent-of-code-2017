from gc import garbage
from typing import List

from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=9)

START_OF_GROUP = "START_OF_GROUP"

def parse(input_data):
    stack = []
    ignore = False
    in_garbage = False
    garbage = ''
    for c in input_data:
        if ignore:
            ignore = False
            # garbage += c
        elif in_garbage and c == '!':
            ignore = True
            # garbage += c
        elif in_garbage and c != '>':
            garbage += c
        elif c == '<':
            garbage = ''
            in_garbage = True
        elif c == '>':
            in_garbage = False
            stack.append(garbage)
        elif c == '{':
            stack.append(START_OF_GROUP)
        elif c == '}':
            group = []
            while len(stack) > 0 and stack[-1] != START_OF_GROUP:
                group.insert(0, stack.pop())
            stack.pop()
            stack.append(group)
        elif c == ',':
            continue
    return stack.pop()


def part1(input_data):
    data = parse(input_data)

    def count_groups(group, lvl):
        counter = 0
        if isinstance(group, list):
            counter += lvl
            for element in group:
                counter += count_groups(element, lvl + 1)
        return counter

    return count_groups(data, 1)


def part2(input_data):
    data = parse(input_data)
    def count_garbage(group):
        counter = 0
        if isinstance(group, list):
            for element in group:
                counter += count_garbage(element)
        elif isinstance(group, str):
            counter += len(group)
        return counter
    return count_garbage(data)

def main():
    assert [] == parse('{}')
    assert [[[]]] == parse('{{{}}}')
    assert [[], []] == parse('{{}{}}')
    assert [[[], [], [[]]]] == parse('{{{},{},{{}}}}')
    assert ['{},{},{{}}'] == parse('{<{},{},{{}}>}')
    assert ['a', 'a', 'a', 'a'] == parse('{<a>,<a>,<a>,<a>}')
    assert [['a'], ['a'], ['a'], ['a']] == parse('{{<a>},{<a>},{<a>},{<a>}}')
    assert [['},{<},{<},{<a']] == parse('{{<!>},{<!>},{<!>},{<a>}}')

    assert 1 == part1('{}')
    assert 6 == part1('{{{}}}')
    assert 5 == part1('{{}{}}')
    assert 16 == part1('{{{},{},{{}}}}')
    assert 1 == part1('{<a>,<a>,<a>,<a>}')
    assert 9 == part1('{{<ab>},{<ab>},{<ab>},{<ab>}}')
    assert 9 == part1('{{<!!>},{<!!>},{<!!>},{<!!>}}')
    assert 3 == part1('{{<!>},{<!>},{<!>},{<a>}}')
    print("part1 example OK")

    puzzle.answer_a = part1(puzzle.input_data)
    print("part1 OK")

    assert 10 == part2('<{o"i!a,<{i<a>')
    print("part2 example OK")

    puzzle.answer_b = part2(puzzle.input_data)
    print("part2 OK")


if __name__ == '__main__':
    main()
