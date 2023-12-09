def main():
    n_steps = 0
    step = 'AAA'
    with open('8.txt') as f:
        data = f.read().split('\n')
    instructions = data[0]
    data = {line[0:3]: [line[7:10], line[12:15]] for line in data[2:]}
    found = False
    while not found:
        for instruction in instructions:
            step = data[step][0] if instruction == 'L' else data[step][1]
            n_steps += 1
            if step == 'ZZZ':
                found = True
                break
    print(n_steps)


if __name__ == '__main__':
    main()
