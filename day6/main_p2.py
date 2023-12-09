def f1(i, n):
    return i*(n-i)


def main():
    with open("6.txt", "r") as f:
        data = f.read().split('\n')
    times = int(''.join([t for t in data[0].strip().split(' ') if t.isdigit()]))
    distances = int(''.join([d for d in data[1].strip().split(' ') if d.isdigit()]))
    r = 0
    for i in range(times+1):
        r += 1 if f1(i, times) > distances else 0
    print(r)


if __name__ == '__main__':
    main()
