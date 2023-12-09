def main():
    result = 0
    with open('4.txt') as f:
        data = f.read().split('\n')
    for line in data:
        numbers = line.split(':')[1].split('|')
        winning_numbers = [int(number) for number in numbers[0].split(' ') if number]
        my_numbers = [int(number) for number in numbers[1].split(' ') if number]
        match_count = sum(1 for number in my_numbers if number in winning_numbers)
        if match_count:
            result += 2**(match_count-1)
    print(result)


if __name__ == '__main__':
    main()
