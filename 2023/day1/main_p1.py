def main():
    r = 0
    with open('1.txt') as f:
        data = f.read().split('\n')
    for line in data:
        # Récupération du premier digit
        for c1 in line:
            if c1.isdigit():
                break
        # Récupération du dernier digit
        for c2 in line[::-1]:
            if c2.isdigit():
                break
        r += int(c1 + c2)
    print(r)


if __name__ == '__main__':
    main()
