def main():
    with open('14.txt') as f:
        data = f.read().split('\n')
    m = [[c for c in line] for line in data]
    I = len(m)
    J = len(m[0])
    c_n = 1000000000
    s = 0
    modified = True
    while modified:
        modified = False
        for i in range(1, I):
            for j in range(J):
                if m[I-1-i+1][j] == 'O' and m[I-1-i][j] == '.':
                    modified = True
                    m[I-1-i+1][j], m[I-1-i][j] = '.', 'O'
    for i, line in enumerate(m):
        s += line.count('O') * (I - i)
    print(s)


if __name__ == '__main__':
    main()
