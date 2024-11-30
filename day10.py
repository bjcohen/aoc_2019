import functools
import math


def cmp_xy(xy1, xy2):
    x1, y1 = xy1
    x2, y2 = xy2
    if x1 == 0 and x2 == 0:
        return 0
    elif x1 == 0:
        return y1
    elif x2 == 0:
        return -y2
    else:
        return y1 / x1 - y2 / x2


if __name__ == "__main__":
    with open("day10.txt") as f:
        grid = [l for l in f]
    w = len(grid[0])
    h = len(grid)
    coords = []
    for y in range(h):
        for x in range(w):
            if grid[y][x] == "#":
                coords.append((x, y))
    coords_set = set(coords)
    max_non_blocked_count = -1
    for x0, y0 in coords:
        non_blocked_count = 0
        for x1, y1 in coords:
            if x0 == x1 and y0 == y1:
                continue
            gcd = math.gcd(x1 - x0, y1 - y0)
            found = False
            for i in range(1, gcd):
                test = (x0 + (x1 - x0) // gcd * i, y0 + (y1 - y0) // gcd * i)
                if test in coords_set:
                    found = True
                    break
            if not found:
                non_blocked_count += 1
        if non_blocked_count > max_non_blocked_count:
            max_non_blocked_count = non_blocked_count
            max_coords = x0, y0
    print(max_non_blocked_count)
    x0, y0 = max_coords
    h1, h2 = {}, {}
    for x1, y1 in coords:
        if (x0, y0) == (x1, y1):
            continue
        gcd = math.gcd(x1 - x0, y1 - y0)
        angle = ((x1 - x0) // gcd, (y1 - y0) // gcd)
        if x1 >= x0:
            h1[angle] = h1.get(angle, [])
            h1[angle].append((x1, y1))
        else:
            h2[angle] = h1.get(angle, [])
            h2[angle].append((x1, y1))
    i = 0
    while i != 200:
        for xy in sorted(h1.keys(), key=functools.cmp_to_key(cmp_xy)):
            if h1[xy]:
                c = h1[xy].pop(0)
                i += 1
                if i == 200:
                    break
        for xy in sorted(h2.keys(), key=functools.cmp_to_key(cmp_xy)):
            if i == 200:
                break
            if h2[xy]:
                c = h2[xy].pop(0)
                i += 1
                if i == 200:
                    break
    print(100 * c[0] + c[1])
