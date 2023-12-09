def f1(i, n):
    return i*(n-i)


def main():
    with open("6.txt", "r") as f:
        data = f.read().split('\n')
    times = [int(t) for t in data[0].strip().split(' ') if t.isdigit()]
    distances = [int(d) for d in data[1].strip().split(' ') if d.isdigit()]
    r = 1
    for j in range(len(times)):
        s = 0
        for i in range(times[j]+1):
            s += 1 if f1(i, times[j]) > distances[j] else 0
        r = r * s
    print(r)


if __name__ == '__main__':
    main()
