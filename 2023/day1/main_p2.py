valid_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

trickys = ['oneight',
           'twone',
           'threeight',
           'fiveight',
           'eighthree',
           'nineight']


def main():
    r = 0
    with open('1.txt') as f:
        data = f.read().split('\n')
    for line in data:
        new_line_for_first_digit = line
        new_line_for_last_digit = line
        # Récupération du premier digit
        while True:
            test = [(i, new_line_for_first_digit.find(valid_digit))
                    for i, valid_digit in enumerate(valid_digits, 1)
                    if new_line_for_first_digit.find(valid_digit) != -1]
            if not test:
                break
            test.sort(key=lambda x: x[1])
            valid_digit = test[0][0]
            new_line_for_first_digit = new_line_for_first_digit.replace(valid_digits[valid_digit - 1],
                                                                        str(valid_digit))
        for c1 in new_line_for_first_digit:
            if c1.isdigit():
                break
        # Récupération du dernier digit
        while True:
            test = [(i, new_line_for_last_digit.rfind(valid_digit))
                    for i, valid_digit in enumerate(valid_digits, 1)
                    if new_line_for_last_digit.rfind(valid_digit) != -1]
            if not test:
                break
            test.sort(key=lambda x: x[1], reverse=True)
            valid_digit = test[0][0]
            new_line_for_last_digit = new_line_for_last_digit.replace(valid_digits[valid_digit - 1],
                                                                      str(valid_digit))
        for c2 in new_line_for_last_digit[::-1]:
            if c2.isdigit():
                break
        r += int(c1+c2)
    print(r)


if __name__ == '__main__':
    main()
