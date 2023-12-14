from itertools import product


def main():
    s = 0
    symbols = ['.', '#']
    with open('12.txt') as f:
        data = f.read().split('\n')
    for line in data:
        ar = line.split(' ')[0]
        p = line.split(' ')[1]
        qm_indexes = [i for i, x in enumerate(ar) if x == "?"]
        combinations = list(list(zip(qm_indexes, element))
                            for element in product(symbols, repeat=len(qm_indexes)))
        for combination in combinations:
            t = ar
            for r in combination:
                t = t[:r[0]] + r[1] + t[r[0] + 1:]
            if ','.join([str(len(c)) for c in t.split('.') if c]) == p:
                s += 1
    print(s)


if __name__ == '__main__':
    main()
