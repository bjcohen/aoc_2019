import intcode
import itertools


if __name__ == "__main__":
    with open("day17.txt") as f:
        prog = intcode.parse(f)

    ic = intcode.run(prog, None)

    grid = "".join(chr(c) for c in ic).split("\n")

    w = len(grid[0])
    h = len(grid) - 2

    intersections = []
    for x in range(w):
        for y in range(h):
            if (
                grid[y][x] == "#"
                and x > 0
                and grid[y][x - 1] == "#"
                and x < len(grid[0]) - 1
                and grid[y][x + 1] == "#"
                and y > 0
                and grid[y - 1][x] == "#"
                and y < len(grid) - 1
                and grid[y + 1][x] == "#"
            ):
                intersections.append((x, y))
    print(sum(x * y for (x, y) in intersections))
    prog[0] = 2

    cx, cy, cd = None, None, None

    for x in range(w):
        for y in range(h):
            if grid[y][x] in ["^", "v", "<", ">"]:
                cx, cy, cd = x, y, grid[y][x]

    path = [(cx, cy, cd, None)]

    print("\n".join(grid))

    while True:
        nds = {
            "^": [("^", "S"), ("<", "L"), (">", "R")],
            "<": [("<", "S"), ("^", "R"), ("v", "L")],
            ">": [(">", "S"), ("^", "L"), ("v", "R")],
            "v": [("v", "S"), ("<", "R"), (">", "L")],
        }[cd]
        nx, ny, nd, instr = None, None, None, None
        for nd, instr in nds:
            vx, vy = {
                "^": (0, -1),
                "<": (-1, 0),
                ">": (1, 0),
                "v": (0, 1),
            }[nd]
            if (
                cy + vy >= 0
                and cy + vy < h
                and cx + vx >= 0
                and cx + vx < w
                and grid[cy + vy][cx + vx] == "#"
            ):
                nx, ny = cx + vx, cy + vy
                break
        if nx is None:
            break
        else:
            cx, cy, cd = nx, ny, nd
            path.append((cx, cy, cd, instr))

    instrs_str = ",".join(
        [
            k if k in ["L", "R"] else str(len(list(g)) + 1)
            for k, g in itertools.groupby(p[3] for p in itertools.islice(path, 1, None))
        ]
    )

    print(instrs_str + "\n")

    main = "A,B,A,C,B,C,A,C,B,C"
    a = "L,8,R,10,L,10"
    b = "R,10,L,8,L,8,L,10"
    c = "L,4,L,6,L,8,L,8"

    inputs = [ord(c) for c in (main + "\n" + a + "\n" + b + "\n" + c + "\n" + "n\n")]

    ic = intcode.run(prog, iter(inputs))
    print([o for o in ic][-1])
