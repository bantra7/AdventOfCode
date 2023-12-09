def get_corresponding_number(n, map_i):
    i = 0
    match = False
    dest_number = n
    while not match and i < len(map_i):
        indexes = [int(c) for c in map_i[i].split(' ')]
        if len(indexes) != 3:
            raise ValueError
        destination_range = indexes[0]
        source_range = indexes[1]
        range_length = indexes[2]
        if source_range <= n < source_range+range_length:
            dest_number = n - source_range + destination_range
            match = True
        i += 1
    return dest_number


def main():
    locations = []
    map_indexs = []
    with open('5.txt') as f:
        lines = [line.strip() for line in f.readlines()]
        seeds = [int(seed) for seed in lines[0].split(':')[1].split()]
        for i in range(2, len(lines)):
            line = lines[i].strip()
            # using any() to check for any occurrence
            if not any(c.isdigit() for c in line) and line:
                map_indexs.append(i)
        map_indexs.append(len(lines))
        maps = [[]] * (len(map_indexs)-1)
        for i in range(len(map_indexs)-1):
            result = []
            for j in range(map_indexs[i]+1, map_indexs[i+1]):
                if lines[j]:
                    result.append(lines[j])
            maps[i] = result
        for seed in seeds:
            location = seed
            for map_i in maps:
                location = get_corresponding_number(location, map_i)
            locations.append(location)
        print(min(locations))


if __name__ == '__main__':
    main()
