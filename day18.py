import heapq


def reachable(grid, x, y, keys):
    queue = [(x, y, 0)]
    seen = set()
    ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while queue:
        cx, cy, d = queue.pop(0)
        if grid[cy][cx].islower() and grid[cy][cx] not in keys:
            yield d, cx, cy, grid[cy][cx]
            continue
        for dx, dy in ds:
            nx, ny = cx + dx, cy + dy
            if ((nx, ny)) in seen:
                continue
            seen.add((nx, ny))

            c = grid[ny][nx]
            if c in [".", "@"] or c.islower() or (c.isupper() and c.lower() in keys):
                queue.append((nx, ny, d + 1))


def solve(grid, pt2=False):
    grid = grid.copy()
    sx, xy = None, None
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "@":
                sx, sy = x, y
    if pt2:
        grid[sy - 1] = grid[sy - 1][:sx] + "#" + grid[sy - 1][sx + 1 :]
        grid[sy] = grid[sy][: sx - 1] + "###" + grid[sy][sx + 2 :]
        grid[sy + 1] = grid[sy + 1][:sx] + "#" + grid[sy + 1][sx + 1 :]
    allkeys = set(c for row in grid for c in row if c.islower())
    if pt2:
        seens = [set(), set(), set(), set()]
        xys = (
            (sx - 1, sy - 1),
            (sx + 1, sy - 1),
            (sx - 1, sy + 1),
            (sx + 1, sy + 1),
        )
    else:
        seens = [set()]
        xys = ((sx, sy),)
    queue = [(0, xys, frozenset())]
    while queue:
        d, xys, keys = heapq.heappop(queue)
        if keys == allkeys:
            return d
        for i, (x, y) in enumerate(xys):
            if (x, y, keys) in seens[i]:
                continue
            seens[i].add((x, y, keys))
            for d_, nx, ny, key in reachable(grid, x, y, keys):
                nxys = xys[0:i] + ((nx, ny),) + xys[i + 1 :]
                heapq.heappush(queue, (d + d_, nxys, keys | set([key])))


if __name__ == "__main__":
    with open("day18.txt") as f:
        grid = [row.strip() for row in f]
    print(
        solve(
            """########################
#...............b.C.D.f#
#.######################
#.....@.a.B.c.d.A.e.F.g#
########################""".split(
                "\n"
            )
        )
    )
    print(solve(grid))
    print(solve(grid, pt2=True))
