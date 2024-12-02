import intcode


if __name__ == "__main__":
    with open("day15.txt") as f:
        prog = intcode.parse(f)
    instrs = []

    def gen():
        while True:
            yield instrs.pop(0)

    ic = intcode.run(prog, gen())
    x, y = 0, 0
    d = 1
    ox, oy = None, None
    seen = set()
    while True:
        seen.add((x, y))
        instrs.append(d)
        resp = next(ic)
        if resp == 0:
            d = {1: 4, 4: 2, 2: 3, 3: 1}[d]
        elif resp == 1:
            dx, dy = {1: (0, -1), 2: (0, 1), 3: (-1, 0), 4: (1, 0)}[d]
            x, y = x + dx, y + dy
            d = {1: 3, 3: 2, 2: 4, 4: 1}[d]
        elif resp == 2:
            ox, oy = x, y
            break
    queue = [(0, 0)]
    dists = {(0, 0): 1}
    while queue:
        x, y = queue.pop(0)
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            cand = (x + dx, y + dy)
            if cand in seen and cand not in dists:
                dists[cand] = dists[x, y] + 1
                queue.append(cand)
    print(dists[(ox, oy)])
    queue = [(ox, oy)]
    ospread = {(ox, oy): 1}
    while queue:
        x, y = queue.pop(0)
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            cand = (x + dx, y + dy)
            if cand in seen and cand not in ospread:
                ospread[cand] = ospread[x, y] + 1
                queue.append(cand)
    print(max(ospread.values()))
