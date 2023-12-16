from tqdm import tqdm
def print_m(m, seens: set):
    R = len(m)
    C = len(m[0])
    mt = [[m[i][j] for j in range(C)] for i in range(R)]
    for i, j in seens:
        mt[i][j] = '#'
    for line in mt:
        print(''.join(line))


def get_score(m, si, sj, start):
    R = len(m)
    C = len(m[0])
    seens = {(0, 0, 2)}
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    tiles = [(si, sj, d) for d in start.get(m[0][0])]
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
    return len(seens)


def main():
    with open('16.txt') as f:
        data = f.read().split('\n')
    m = [[c for c in line] for line in data]
    scores = []
    R = len(m)
    C = len(m[0])
    # 0:up, 1:right, 2:down, 3:left
    start_right = {
        '.': 1,
        '-': 1,
        '|': 2,
        '\\': 2,
        '/': 0,
    }
    start_up = {
        '.': [0],
        '-': [1, 3],
        '|': [0],
        '\\': [3],
        '/': [1],
    }
    start_down = {
        '.': [0],
        '-': [1, 3],
        '|': [0],
        '\\': [1],
        '/': [3],
    }
    for i in tqdm(range(R)):
        s = get_score(m, i, 0, start_down)
        scores.append(s)
    for i in tqdm(range(R)):
        s = get_score(m, i, C-1, start_up)
        scores.append(s)
    print(max(scores))


if __name__ == '__main__':
    # 8754
    main()
