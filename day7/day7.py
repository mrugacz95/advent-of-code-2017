from collections import Counter
from itertools import count
from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=7)


def parse(input_data):
    tower = {}
    weights = {}
    for line in input_data.split("\n"):
        if " -> " in line:
            parent, children = line.split(' -> ')
            children = list(children.split(', '))
        else:
            parent = line
            children = []
        parent_name, weight = parent.split(' ')
        weight = int(weight[1:-1])
        tower[parent_name] = children
        weights[parent_name] = weight
    return tower, weights


def part1(input_data):
    tower, weights = parse(input_data)
    parents = {}
    for parent, children in tower.items():
        for child in children:
            parents[child] = parent
    base = (set(parents.values()).difference(set(parents.keys()))).pop()
    return base


def part2(input_data):
    base = part1(input_data)
    tower, weights = parse(input_data)
    sum_weights = {}
    balanced = {}
    parent = {}

    def dfs(node):
        child_weights = []
        for child in tower[node]:
            child_weights.append(dfs(child))
            parent[child] = node
        balanced[node] = len(set(child_weights)) == 1
        weight = weights[node] + sum(child_weights)
        sum_weights[node] = weight
        return weight

    dfs(base)

    node = base
    while not balanced[node]:
        for child in tower[node]:
            if not balanced[child]:
                node = child
                break
        else:
            break

    children = tower[node]
    children_weights = list(map(lambda c: sum_weights[c], children))
    counted = Counter(children_weights)
    wrong_weight = next((k for k, v in counted.items() if v == 1))
    wrong_node = next((node for node, weight in sum_weights.items() if weight == wrong_weight))
    correct_weight = next((k for k, v in counted.items() if v != 1))
    diff = wrong_weight - correct_weight
    return weights[wrong_node] - diff


def main():
    assert 'tknk' == part1(puzzle.examples[0].input_data)
    print("part1 example OK")

    puzzle.answer_a = part1(puzzle.input_data)
    print("part1 OK")

    assert 60 == part2(puzzle.examples[0].input_data)
    print("part2 example OK")

    puzzle.answer_b = part2(puzzle.input_data)
    print("part2 OK")


if __name__ == '__main__':
    main()
