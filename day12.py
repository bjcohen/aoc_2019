import itertools
import math


def run(n, moons_orig):
    moons = moons_orig.copy()
    x1c, x2c, x3c = None, None, None
    for t in itertools.islice(itertools.count(0), n):
        for i, (x1, x2, x3, v1, v2, v3) in enumerate(moons):
            for j, (y1, y2, y3, w1, w2, w3) in enumerate(moons):
                if i >= j:
                    continue
                if x1 > y1:
                    v1 -= 1
                    w1 += 1
                elif x1 < y1:
                    v1 += 1
                    w1 -= 1
                if x2 > y2:
                    v2 -= 1
                    w2 += 1
                elif x2 < y2:
                    v2 += 1
                    w2 -= 1
                if x3 > y3:
                    v3 -= 1
                    w3 += 1
                elif x3 < y3:
                    v3 += 1
                    w3 -= 1
                moons[i] = (x1, x2, x3, v1, v2, v3)
                moons[j] = (y1, y2, y3, w1, w2, w3)
        moons = [
            (x1 + v1, x2 + v2, x3 + v3, v1, v2, v3)
            for (x1, x2, x3, v1, v2, v3) in moons
        ]
        if all(m[0] == mo[0] and m[3] == mo[3] for m, mo in zip(moons, moons_orig)):
            x1c = t + 1
        if all(m[1] == mo[1] and m[4] == mo[4] for m, mo in zip(moons, moons_orig)):
            x2c = t + 1
        if all(m[2] == mo[2] and m[5] == mo[5] for m, mo in zip(moons, moons_orig)):
            x3c = t + 1
        if x1c is not None and x2c is not None and x3c is not None:
            break
    return moons, (x1c, x2c, x3c)


if __name__ == "__main__":
    with open("day12.txt") as f:
        moons = [
            (int(p[0][2:]), int(p[1][2:]), int(p[2][2:]), 0, 0, 0)
            for p in (p[1:-2].split(", ") for p in f)
        ]
    moons1, _ = run(1000, moons)
    print(
        sum(
            (abs(x1) + abs(x2) + abs(x3)) * (abs(v1) + abs(v2) + abs(v3))
            for x1, x2, x3, v1, v2, v3 in moons1
        )
    )
    _, (x1c, x2c, x3c) = run(None, moons)
    print(math.lcm(x1c, x2c, x3c))
