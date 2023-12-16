def print_m(m, seens: set):
    R = len(m)
    C = len(m[0])
    mt = [[m[i][j] for j in range(C)] for i in range(R)]
    for i, j in seens:
        mt[i][j] = '#'
    for line in mt:
        print(''.join(line))


def main():
    with open('16.txt') as f:
        data = f.read().split('\n')
    m = [[c for c in line] for line in data]
    R = len(m)
    C = len(m[0])
    # 0:up, 1:right, 2:down, 3:left
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    seens = {(0, 0, 2)}
    start_right = {
        '.': 1,
        '-': 1,
        '|': 2,
        '\\': 2,
        '/': 0,
    }
    tiles = [(0, 0, start_right.get(m[0][0]))]
    new = True
    while new:
        new = False
        for i in range(len(tiles)):
            ti, tj, d = tiles[0]
            del tiles[0]
            ti += dr[d]
            tj += dc[d]
            if 0 <= ti < R and 0 <= tj < C and (ti, tj, d) not in seens:
                if (ti, tj, d) not in seens:
                    new = True
                    seens.add((ti, tj, d))
                if m[ti][tj] == '|' and d in [1, 3]:
                    tiles.append((ti, tj, 0))
                    tiles.append((ti, tj, 2))
                elif m[ti][tj] == '-' and d in [0, 2]:
                    tiles.append((ti, tj, 1))
                    tiles.append((ti, tj, 3))
                elif m[ti][tj] == '\\':
                    nd = [3, 2, 1, 0]
                    tiles.append((ti, tj, nd[d]))
                elif m[ti][tj] == '/':
                    nd = [1, 0, 3, 2]
                    tiles.append((ti, tj, nd[d]))
                elif m[ti][tj] in ['.', '-', '|']:
                    tiles.append((ti, tj, d))
    seens = set((i, j) for (i, j, d) in seens)
    print_m(m, seens)
    print(len(seens))


if __name__ == '__main__':
    main()
