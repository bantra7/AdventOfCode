def main():
    with open('9.txt') as f:
        data = f.read().split('\n')
    s = 0
    for line in data:
        extrapolate = [[int(number) for number in line.split(' ')]]
        r = []
        for numbers in extrapolate:
            r.append(extrapolate[-1][0])
            if not all(v == 0 for v in numbers):
                extrapolate.append([numbers[i+1]-numbers[i] for i in range(len(numbers)-1)])
        pre_s = 0
        for i in range(len(r)):
            pre_s = r[len(r)-1-i] - pre_s
        s += pre_s
    print(s)


if __name__ == '__main__':
    main()
