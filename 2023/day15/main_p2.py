def get_hash(v, c):
    return (v+ord(c))*17 % 256


def main():
    with open('15.txt') as f:
        data = f.read().split('\n')[0]
    d = [{} for _ in range(256)]
    s = 0
    for h in data.split(','):
        hash = 0
        if '=' in h:
            for c in h.split('=')[0]:
                hash = get_hash(hash, c)
            d[hash][h.split('=')[0]] = h[-1]
        elif '-' in h:
            for c in h.split('-')[0]:
                hash = get_hash(hash, c)
            if d[hash].get(h.split('-')[0]):
                del d[hash][h.split('-')[0]]
    for i, d_i in enumerate(d, 1):
        for j, k in enumerate(d_i.items(), 1):
            s += i * j * int(k[1])
    print(s)


if __name__ == '__main__':
    main()
