import intcode


def run(start):
    x, y, d = (0, 0, "u")
    painted = {}

    def gen_in():
        queue = [start]
        while True:
            x = yield queue[0]
            if x is None:
                queue.pop(0)
            else:
                queue.append(x)

    in_ = gen_in()
    ic = intcode.run(prog, in_)
    while True:
        try:
            paint = next(ic)
            turn = next(ic)
        except StopIteration:
            break
        painted[(x, y)] = paint
        d = {
            ("u", 0): "l",
            ("r", 0): "u",
            ("d", 0): "r",
            ("l", 0): "d",
            ("u", 1): "r",
            ("r", 1): "d",
            ("d", 1): "l",
            ("l", 1): "u",
        }[(d, turn)]
        dx, dy = {
            "u": (0, -1),
            "r": (1, 0),
            "d": (0, 1),
            "l": (-1, 0),
        }[d]
        x += dx
        y += dy
        in_.send(painted.get((x, y), 0))
    return painted


if __name__ == "__main__":
    with open("day11.txt") as f:
        prog = intcode.parse(f)
    print(len(run(0)))
    painted = run(1)
    minx, miny = 0, 0
    maxx, maxy = 0, 0
    for x, y in painted:
        minx, miny, maxx, maxy = min(x, minx), min(y, miny), max(x, maxx), max(y, maxy)
    grid = [[" " for _ in range(maxx - minx + 1)] for _ in range(maxy - miny + 1)]
    for (x, y), p in painted.items():
        grid[y - miny][x - minx] = "#" if p == 0 else " "
    print("\n".join("".join(row) for row in grid))
