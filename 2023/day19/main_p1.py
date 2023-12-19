import re


def interpreter_string(rating):
    pattern = r'{x=(\d+),m=(\d+),a=(\d+),s=(\d+)}'
    matches = re.match(pattern, rating)

    if matches:
        x, m, a, s = map(int, matches.groups())
        return x, m, a, s
    else:
        raise ValueError("Format de chaîne invalide")


def main():
    with open('19.txt') as f:
        data = f.read().split('\n\n')
    workflows = data[0].split('\n')
    ratings = data[1].split('\n')
    D = {}
    for workflow in workflows:
        w_name, rules = workflow.split('{')
        D[w_name] = rules[0:-1].split(',')
    score = 0
    for rating in ratings:
        x, m, a, s = interpreter_string(rating)
        result = 'in'
        while result not in ['A', 'R']:
            modified = False
            for rule in D[result][0:-1]:
                rule_cond, rule_result = rule.split(':')
                if eval(rule_cond, {"x": x, "m": m, "a": a, "s": s}):
                    result = rule_result
                    modified = True
                    break
            if not modified:
                result = D[result][-1]
        if result == 'A':
            score += x+m+a+s
    print(score)


if __name__ == '__main__':
    main()
