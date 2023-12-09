def main():
    score = 0
    with open('1.txt') as f:
        data = f.read().split('\n')
    for line in data:
        digits = []
        for i, c in enumerate(line):
            if c.isdigit():
                digits.append(c)
            for d, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'], 1):
                if line[i:].startswith(val):
                    digits.append(str(d))
        score += int(digits[0] + digits[-1])
    print(score)


if __name__ == '__main__':
    main()
