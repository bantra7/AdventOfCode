def get_hash(v, c):
    return (v+ord(c))*17 % 256


def main():
    with open('15.txt') as f:
        data = f.read().split('\n')[0]
    s = 0
    for h in data.split(','):
        hash = 0
        for c in h:
            hash = get_hash(hash, c)
        s += hash
    print(s)


if __name__ == '__main__':
    main()
