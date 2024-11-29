import sys


def wire_to_coords(wire):
    curr = (0, 0)
    coords = []
    totalsteps = 0
    for d in wire.split(","):
        x1, y1 = curr
        nsteps = int(d[1:])
        n = {
            "U": (x1, y1 + nsteps),
            "R": (x1 + nsteps, y1),
            "D": (x1, y1 - nsteps),
            "L": (x1 - nsteps, y1),
        }[d[0]]
        coords.append((curr, n, totalsteps))
        curr = n
        totalsteps += nsteps
    return coords


if __name__ == "__main__":
    with open("day3.txt") as f:
        wire1, wire2 = f.read().strip().split("\n")
    coords1 = wire_to_coords(wire1)
    coords2 = wire_to_coords(wire2)
    min_dist = sys.maxsize
    for (x11, y11), (x12, y12), _ in coords1:
        for (x21, y21), (x22, y22), _ in coords2:
            if (x11, y11) == (0, 0) and (x21, y21) == (0, 0):
                continue
            if (
                x11 == x12
                and min(x21, x22) <= x11 <= max(x21, x22)
                and y21 == y22
                and min(y11, y12) <= y21 <= max(y11, y12)
            ):
                min_dist = min(min_dist, abs(x11) + abs(y21))
            elif (
                y11 == y12
                and min(y21, y22) <= y11 <= max(y21, y22)
                and x21 == x22
                and min(x11, x12) <= x21 <= max(x11, x12)
            ):
                min_dist = min(min_dist, abs(x21) + abs(y11))
    print(min_dist)
    min_dist = sys.maxsize
    for (x11, y11), (x12, y12), totalsteps1 in coords1:
        for (x21, y21), (x22, y22), totalsteps2 in coords2:
            if (x11, y11) == (0, 0) and (x21, y21) == (0, 0):
                continue
            if (
                x11 == x12
                and min(x21, x22) <= x11 <= max(x21, x22)
                and y21 == y22
                and min(y11, y12) <= y21 <= max(y11, y12)
            ):
                min_dist = min(
                    min_dist,
                    totalsteps1 + totalsteps2 + abs(x11 - x21) + abs(y21 - y11),
                )
            elif (
                y11 == y12
                and min(y21, y22) <= y11 <= max(y21, y22)
                and x21 == x22
                and min(x11, x12) <= x21 <= max(x11, x12)
            ):
                min_dist = min(
                    min_dist,
                    totalsteps1 + totalsteps2 + abs(y11 - y21) + abs(x21 - x11),
                )
    print(min_dist)
