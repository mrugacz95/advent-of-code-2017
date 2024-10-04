from collections import defaultdict

from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=12)


def parse(input_data):
    graph = defaultdict(set)
    for line in input_data.split("\n"):
        node_from, nodes_to = line.split(' <-> ')
        for node in nodes_to.split(', '):
            graph[node_from].add(node)
    return graph


def part1(input_data):
    graph = parse(input_data)
    vis = set()
    def dfs(node):
        if node in vis:
            return
        vis.add(node)
        for node in graph[node]:
            dfs(node)
    dfs('0')
    return len(vis)


def part2(input_data):
    graph = parse(input_data)
    groups = 0
    global_vis = set()
    def reach_all_in_group(start_node):
        vis = set()
        def dfs(node):
            if node in vis or node in global_vis:
                return
            vis.add(node)
            global_vis.add(node)
            for node in graph[node]:
                dfs(node)
        dfs(start_node)
        new_group = 1 if len(vis) != 0 else 0
        return new_group
    for group_node in graph.keys():
        groups += reach_all_in_group(group_node)
    return groups


def main():
    assert 6 == part1(puzzle.examples[0].input_data)
    print("part1 example OK")

    puzzle.answer_a = part1(puzzle.input_data)
    print("part1 OK")

    assert 2 == part2(puzzle.examples[0].input_data)
    print("part2 example OK")

    puzzle.answer_b = part2(puzzle.input_data)
    print("part2 OK")


if __name__ == '__main__':
    main()
