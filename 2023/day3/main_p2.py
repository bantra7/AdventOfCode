import re


def get_neighbours(i, r, f_length, line_length):
    n = []
    for j in r:
        if i == 0:
            n.append((i + 1, j))
        elif i == f_length:
            n.append((i - 1, j))
        else:
            n.append((i - 1, j))
            n.append((i + 1, j))
    n.append((i, min(r)))
    n.append((i, max(r)))
    return [(i, j) for (i, j) in n if 0 <= j < line_length and 0 <= i < f_length]


def main():
    numbers = {}
    with open('3.txt') as f:
        data = f.read().split('\n')
    matrix = [[c for c in line.strip()] for line in data]
    f_length = len(data)
    for i, line in enumerate(data):
        line = line.strip()
        line_length = len(line)
        d = [(int(m.group()),
              get_neighbours(i, range(m.start() - 1, m.start() + len(m.group()) + 1), f_length, line_length))
             for m in re.finditer(r'\d+', line)]
        for number, neighbours in d:
            for p, q in neighbours:
                if matrix[p][q] == '*':
                    if numbers.get(f'({p},{q})'):
                        numbers[f'({p},{q})'].append(number)
                    else:
                        numbers[f'({p},{q})'] = [number]
    numbers = [v[0] * v[1] for k, v in numbers.items() if len(v) == 2]
    print(sum(numbers))


if __name__ == '__main__':
    main()
