import re
import sys
from collections import defaultdict
from email.policy import default

from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=8)


def parse(input_data):
    commands = []
    for line in input_data.split("\n"):
        match = re.search(r'([a-z]+) (inc|dec) (-?\d+) if ([a-z]+) (==|>|<|<=|>=|!=) (-?\d+)', line)
        reg = match.group(1)
        op = match.group(2)
        val = int(match.group(3))
        lhs = match.group(4)
        comp = match.group(5)
        rhs = int(match.group(6))
        command = (reg, op, val, lhs, comp, rhs)
        commands.append(command)
    return commands


def step(registers, command):
    reg, op, val, lhs, comp, rhs = command
    condition = {
        '>': lambda: registers[lhs] > rhs,
        '<': lambda: registers[lhs] < rhs,
        '==': lambda: registers[lhs] == rhs,
        '<=': lambda: registers[lhs] <= rhs,
        '>=': lambda: registers[lhs] >= rhs,
        '!=': lambda: registers[lhs] != rhs,
    }.get(comp)
    if condition():
        def inc():
            registers[reg] += val

        def dec():
            registers[reg] -= val

        command = {
            'inc': inc,
            'dec': dec,
        }.get(op)
        command()


def part1(input_data):
    commands = parse(input_data)
    registers = defaultdict(int)
    for command in commands:
        step(registers, command)
    return max(registers.values())


def part2(input_data):
    commands = parse(input_data)
    registers = defaultdict(int)
    max_value = -sys.maxsize
    for command in commands:
        step(registers, command)
        max_value = max(max_value, *registers.values())
    return max_value


def main():
    assert 1 == part1(puzzle.examples[0].input_data)
    print("part1 example OK")

    puzzle.answer_a = part1(puzzle.input_data)
    print("part1 OK")

    assert 10 == part2(puzzle.examples[0].input_data)
    print("part2 example OK")

    puzzle.answer_b = part2(puzzle.input_data)
    print("part2 OK")


if __name__ == '__main__':
    main()
