import re

BALLS = [12, 13, 14]
BALL_TYPES = ['red', 'green', 'blue']


def get_balls_from_set(game_set):
    result = [0, 0, 0]
    for ball_input in game_set.split(','):
        ball_number = int(ball_input.split(' ')[1])
        ball_type = ball_input.split(' ')[2]
        result[BALL_TYPES.index(ball_type)] += ball_number
    return result


def main():
    r = 0
    with open('2.txt') as f:
        data = f.read().split('\n')
    for line in data:
        game_id = int(re.findall(r'\d+', line.split(':')[0])[0])
        game_sets = line.split(':')[1].split(';')
        game_set_balls = [get_balls_from_set(game_set) for game_set in game_sets]
        game_over = False
        for game_set in game_set_balls:
            for i in range(3):
                if game_set[i] > BALLS[i]:
                    game_over = True
        if not game_over:
            r += game_id
    print(r)


if __name__ == '__main__':
    main()
