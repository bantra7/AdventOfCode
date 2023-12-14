import numpy as np


def get_score(m):
    for i in range(1, len(m)):
        if i < len(m) / 2:
            t1 = m[0:i]
            t2 = m[i:][0:i][::-1]
        else:
            t1 = m[::-1][0:len(m) - i]
            t2 = m[::-1][len(m) - i:][0:len(m) - i][::-1]
        total_mismatches = 0
        for top_row, bottom_row in zip(t1, t2):
            for (top_char, bottom_char) in zip(top_row, bottom_row):
                if top_char != bottom_char:
                    total_mismatches += 1
        if total_mismatches == 1:
            return i
    return 0


def main():
    with open('13.txt') as f:
        data = f.read().split('\n\n')
    hs = 0
    vs = 0
    for b_i, b in enumerate(data, 1):
        m = [c for c in b.split('\n')]
        m1 = [[s for s in l] for l in m]
        mtx = np.array(m1)
        m_t = [''.join(l) for l in mtx.transpose()]
        hs += get_score(m)
        vs += get_score(m_t)
    s = hs*100+vs
    print(s)


if __name__ == '__main__':
    main()
