import math
from itertools import cycle


def main():
    with open('8.txt') as f:
        data = f.read().split('\n')
    instructions = data[0]
    data = {line[0:3]: [line[7:10], line[12:15]] for line in data[2:]}
    nodes = [k for k, v in data.items() if k[2] == 'A']
    steps = [0] * len(nodes)
    for i, n in enumerate(nodes):
        pos = n
        for instruction in cycle(instructions):
            pos = data[pos][0] if instruction == 'L' else data[pos][1]
            steps[i] += 1
            if pos.endswith('Z'):
                break
    print(math.lcm(*steps))


if __name__ == '__main__':
    main()
