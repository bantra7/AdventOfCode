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
        game_sets = line.split(':')[1].split(';')
        game_set_balls = [get_balls_from_set(game_set) for game_set in game_sets]
        red_balls = [int(game_set_ball[0]) for game_set_ball in game_set_balls]
        green_balls = [int(game_set_ball[1]) for game_set_ball in game_set_balls]
        blue_balls = [int(game_set_ball[2]) for game_set_ball in game_set_balls]
        r += (max(red_balls) * max(green_balls) * max(blue_balls))
    print(r)


if __name__ == '__main__':
    main()
