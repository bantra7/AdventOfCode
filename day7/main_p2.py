
CARDS = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

RANKS = ['[1, 1, 1, 1, 1]',
         '[1, 1, 1, 2]',
         '[1, 2, 2]',
         '[1, 1, 3]',
         '[2, 3]',
         '[1, 4]',
         '[5]']


def is_better(cards_i, cards):
    for i in range(5):
        if CARDS.index(cards_i[i]) == CARDS.index(cards[i]):
            continue
        return CARDS.index(cards_i[i]) > CARDS.index(cards[i])


def get_type(cards):
    d = {}
    n_j = 0
    for card in cards:
        if card == 'J':
            n_j += 1
        else:
            if d.get(card):
                d[card] += 1
            else:
                d[card] = 1
    l = list(d.values())
    l.sort()
    if l:
        l[-1] += n_j
    else:
        return [5]
    return l


def main():
    with open('7.txt') as f:
        data = f.read().split('\n')
    r = {}
    for hand in data:
        cards, bid = tuple(hand.split(' '))
        hand_type = str(get_type(cards))
        if r.get(hand_type):
            inserted = False
            n = len(r[hand_type])
            i = 0
            while not inserted and i < n:
                # On compare la nouvelle main avec r[hand_type][i]
                # Si elle est mieux on ne l'insère pas et sinon on l'insère
                if not is_better(cards, r[hand_type][i][0]):
                    inserted = True
                    r[hand_type].insert(i, (cards, bid))
                i += 1
            if not inserted:
                r[hand_type].append((cards, bid))
        else:
            r[hand_type] = [(cards, bid)]
    order = []
    for rank in RANKS:
        if r.get(rank):
            order += r[rank]
    score = 0
    for i, (hand, bid) in enumerate(order, 1):
        score += i * int(bid)
    print(score)


if __name__ == '__main__':
    main()
