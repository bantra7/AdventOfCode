def main():
    score = 0
    with open('1.txt') as f:
        data = f.read().split('\n')
    for line in data:
        digits = []
        for c in line:
            if c.isdigit():
                digits.append(c)
        score += int(digits[0] + digits[-1])
    print(score)


if __name__ == '__main__':
    main()
