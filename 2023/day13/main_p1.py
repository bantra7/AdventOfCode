import numpy as np


def get_score(m):
    r = 0
    for i in range(1, len(m)):
        if i < len(m) / 2:
            t1 = m[0:i]
            t2 = m[i:][0:i][::-1]
        else:
            t1 = m[::-1][0:len(m) - i]
            t2 = m[::-1][len(m) - i:][0:len(m) - i][::-1]
        if t1 == t2:
            r = i
            break
    return r


def main():
    with open('13.txt') as f:
        data = f.read().split('\n\n')
    hs = 0
    vs = 0
    for b in data:
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
