import tqdm
from aocd.models import Puzzle

puzzle = Puzzle(year=2017, day=13)


def parse(input_data):
    data = {}
    for line in input_data.split("\n"):
        id, depth = map(int, line.split(': '))
        data[id] = depth
    return data


def display_state(data, scanner_pos, pos, second):
    max_layer = max(scanner_pos.keys())
    max_depth = max(data.values())
    print(f'Picosecond {second}:')
    for depth in range(-1, max_depth):
        for layer in range(max_layer + 1):
            if depth == -1:
                print(f'  {layer} ', end='')
                continue
            if layer not in data.keys() and depth == 0:
                if pos == layer:
                    print(' (.)', end='')
                else:
                    print(' ...', end='')
                continue
            if layer not in data.keys() or depth >= data[layer]:
                print(f'    ', end='')
                continue
            c = 'S' if scanner_pos[layer] == depth else ' '
            if pos == layer and depth == 0:
                print(f' ({c})', end='')
            else:
                print(f' [{c}]', end='')
        print()
    print()


def part1(input_data):
    layers = parse(input_data)
    scanner_pos = {k: 0 for k, v in layers.items()}
    scanner_dir = {k: True for k, v in layers.items()}
    max_layer = max(scanner_pos.keys())
    caught = 0
    for pos in range(max_layer + 1):
        # display_state(layers, scanner_pos, pos, pos)
        if pos in scanner_pos.keys() and scanner_pos[pos] == 0:
            caught += pos * layers[pos]
        for layer, layer_pos in scanner_pos.items():
            if layer_pos == 0:
                scanner_dir[layer] = True
            elif layer_pos == layers[layer] - 1:
                scanner_dir[layer] = False
            delta = 1 if scanner_dir[layer] else -1
            scanner_pos[layer] = layer_pos + delta
    return caught


def part2_slow(input_data):
    layers = parse(input_data)

    scanner_pos = {k: 0 for k, v in layers.items()}
    scanner_dir = {k: True for k, v in layers.items()}

    def delay_packet(scanner_pos, scanner_dir):
        for layer, layer_pos in scanner_pos.items():
            if layer_pos == 0:
                scanner_dir[layer] = True
            elif layer_pos == layers[layer] - 1:
                scanner_dir[layer] = False
            delta = 1 if scanner_dir[layer] else -1
            scanner_pos[layer] = layer_pos + delta
        return scanner_pos, scanner_dir

    max_layer = max(layers.keys())

    def simulate(scanner_pos, scanner_dir):
        for pos in range(max_layer + 1):
            if pos in scanner_pos.keys() and scanner_pos[pos] == 0:
                return True
            for layer, layer_pos in scanner_pos.items():
                if layer_pos == 0:
                    scanner_dir[layer] = True
                elif layer_pos == layers[layer] - 1:
                    scanner_dir[layer] = False
                delta = 1 if scanner_dir[layer] else -1
                scanner_pos[layer] = layer_pos + delta
        return False

    delay = 0
    progres = tqdm.tqdm()
    while True:
        progres.update(1)
        delay += 1
        scanner_pos, scanner_dir = delay_packet(scanner_pos, scanner_dir)
        caught = simulate(scanner_pos.copy(), scanner_dir.copy())
        if not caught:
            break
    return delay


def mod(x, p):
    return ((x % p) + p) % p


def part2_fast(input_data):
    delay = 0
    progres = tqdm.tqdm()
    layers = parse(input_data)
    while True:
        progres.update(1)
        def simulate():
            for layer, depth in layers.items():
                x = delay + layer
                p = depth - 1
                y = 2 * abs(mod(x / 2 , p) - p / 2) - p # triangle wave function
                if y == 0:
                    return False
            return True
        if simulate():
            break
        delay += 1
    return delay


def main():
    assert 24 == part1(puzzle.examples[0].input_data)
    print("part1 example OK")

    puzzle.answer_a = part1(puzzle.input_data)
    print("part1 OK")

    assert 10 == part2_slow(puzzle.examples[0].input_data)
    print("part2 slow example OK")

    assert 10 == part2_fast(puzzle.examples[0].input_data)
    print("part2 fast example OK")

    puzzle.answer_b = part2_fast(puzzle.input_data)
    print("part2 OK")


if __name__ == '__main__':
    main()
