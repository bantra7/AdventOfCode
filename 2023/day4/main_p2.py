import re


def main():
    with open('4.txt') as f:
        data = f.read().split('\n')
    cards = [1] * len(data)
    for line in data:
        pattern = r'Card\s+(\d+)'
        card_id = int(re.search(pattern, line).group(1))
        numbers = line.split(':')[1].split('|')
        winning_numbers = [int(number) for number in numbers[0].split(' ') if number]
        my_numbers = [int(number) for number in numbers[1].split(' ') if number]
        match_count = sum(1 for number in my_numbers if number in winning_numbers)
        for j in range(cards[card_id-1]):
            for i in range(card_id, card_id+match_count):
                if i < len(cards):
                    cards[i] += 1
    print(sum(cards))


if __name__ == '__main__':
    main()
