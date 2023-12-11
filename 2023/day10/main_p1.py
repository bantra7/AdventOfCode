def main():
    with open('10.txt') as f:
        data = f.read().split('\n')
    mtx = [[j for j in line] for line in data]
    n = len(mtx)
    p = len(mtx[0])
    # On va remplacer le S par un type de tuyau
    for i in range(n):
        for j in range(p):
            if mtx[i][j] == 'S':
                si, sj = i, j
                up_valid = (mtx[i - 1][j] in ['|', '7', 'F'])
                right_valid = (mtx[i][j + 1] in ['-', '7', 'J'])
                down_valid = (mtx[i + 1][j] in ['|', 'L', 'J'])
                left_valid = (mtx[i][j - 1] in ['-', 'L', 'F'])
                assert sum([up_valid, right_valid, down_valid, left_valid]) == 2
                if up_valid and down_valid:
                    mtx[i][j] = '|'
                    sd = 0
                elif up_valid and right_valid:
                    mtx[i][j] = 'L'
                    sd = 0
                elif up_valid and left_valid:
                    mtx[i][j] = 'J'
                    sd = 0
                elif down_valid and right_valid:
                    mtx[i][j] = 'F'
                    sd = 2
                elif down_valid and left_valid:
                    mtx[i][j] = '7'
                    sd = 2
                elif left_valid and right_valid:
                    mtx[i][j] = '-'
                    sd = 1
    # 0:up, 1:right, 2:down, 3:left
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    nb = 0
    d = sd
    pi = si
    pj = sj
    while True:
        nb += 1
        pi += dr[d]
        pj += dc[d]
        if mtx[pi][pj] == 'L':
            if d == 3:
                d = 0
            elif d == 2:
                d = 1
        elif mtx[pi][pj] == 'J':
            if d == 1:
                d = 0
            elif d == 2:
                d = 3
        elif mtx[pi][pj] == '7':
            if d == 0:
                d = 3
            elif d == 1:
                d = 2
        elif mtx[pi][pj] == 'F':
            if d == 0:
                d = 1
            elif d == 3:
                d = 2
        if (pi, pj) == (si, sj):
            print(nb // 2)
            break


if __name__ == '__main__':
    main()
