import numpy as np
from itertools import combinations


def main(space):
    with open('11.txt') as f:
        data = f.read().split('\n')
    m = [[c for c in line] for line in data]
    n = len(m)
    p = len(m[0])
    mtx = np.array(m)
    empty_rows = [i for i, r in enumerate(mtx) if all(c == '.' for c in r)]
    empty_cols = [i for i, r in enumerate(mtx.transpose()) if all(c == '.' for c in r)]
    stars = []
    for i, r in enumerate(mtx):
        for j, c in enumerate(r):
            if c == '#':
                stars.append((i, j))
    stars = combinations(stars, 2)
    s = 0
    for ((x1, y1), (x2, y2)) in stars:
        if x1 >= x2:
            d_i = [space if i in empty_rows else 1 for i in range(n)][x2:x1]
        else:
            d_i = [space if i in empty_rows else 1 for i in range(n)][x1:x2]
        if y1 >= y2:
            d_j = [space if i in empty_cols else 1 for i in range(p)][y2:y1]
        else:
            d_j = [space if i in empty_cols else 1 for i in range(p)][y1:y2]
        s += sum(d_i) + sum(d_j)
    return s


if __name__ == '__main__':
    # Part 1
    print(f'Part 1 Solution: {main(2)}')
    # Part 2
    print(f'Part 2 Solution: {main(1000000)}')
