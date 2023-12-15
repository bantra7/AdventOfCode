def roll(m):
    modified = True
    while modified:
        modified = False
        for i in range(1, len(m)):
            for j in range(len(m[0])):
                if m[len(m) - 1 - i + 1][j] == 'O' and m[len(m) - 1 - i][j] == '.':
                    modified = True
                    m[len(m) - 1 - i + 1][j], m[len(m) - 1 - i][j] = '.', 'O'
    return m


def get_score(m):
    s = 0
    for i, line in enumerate(m):
        s += line.count('O') * (len(m) - i)
    return s


def rotate(m):
    nm = [['*' for _ in range(len(m))] for _ in range(len(m[0]))]
    for i in range(len(m)):
        for j in range(len(m[0])):
            nm[j][len(m) - 1 - i] = m[i][j]
    return nm


def main():
    with open('14.txt') as f:
        data = f.read().split('\n')
    m = [[c for c in line] for line in data]
    t = 0
    target = 1000000000
    grids = {}
    while t < target:
        t += 1
        for i in range(4):
            m = roll(m)
            m = rotate(m)
        mh = tuple(tuple(row) for row in m)
        if mh in grids:
            cycle_length = t - grids[mh]
            amt = (target - t) // cycle_length
            t += amt * cycle_length
        grids[mh] = t
    print(get_score(m))


if __name__ == '__main__':
    main()
