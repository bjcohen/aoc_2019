import heapq

if __name__ == "__main__":
    with open("day20.txt") as f:
        grid = f.read().strip("\n").split("\n")
    h = len(grid)
    w = len(grid[0])
    nlt = [" ", "#", "."]
    portals = {}
    entrances = {}
    for y in range(h):
        for x in range(w):
            if grid[y][x] not in nlt and y < h - 1 and grid[y + 1][x] not in nlt:
                label = grid[y][x] + grid[y + 1][x]
                entrance = None
                inout = (
                    "outer" if x == 0 or x == w - 2 or y == 0 or y == h - 2 else "inner"
                )
                if y < h - 2 and grid[y + 2][x] == ".":
                    entrance = x, y + 1, "v", inout
                elif y > 1 and grid[y - 1][x] == ".":
                    entrance = x, y, "^", inout
                portals[label] = portals.get(label, [])
                portals[label].append(entrance)
                entrances[entrance[:2]] = label, inout
            if grid[y][x] not in nlt and x < w - 1 and grid[y][x + 1] not in nlt:
                label = grid[y][x] + grid[y][x + 1]
                entrance = None
                inout = (
                    "outer" if x == 0 or x == w - 2 or y == 0 or y == h - 2 else "inner"
                )
                if x < w - 2 and grid[y][x + 2] == ".":
                    entrance = x + 1, y, ">", inout
                elif x > 1 and grid[y][x - 1] == ".":
                    entrance = x, y, "<", inout
                portals[label] = portals.get(label, [])
                portals[label].append(entrance)
                entrances[entrance[:2]] = label, inout

    start = portals["AA"][0][:3]
    del portals["AA"]
    del portals["ZZ"]

    dists = {}
    queue = [("AA", "outer", *start, 0)]
    exited = {("AA", "inner"), ("ZZ", "inner")}

    d_dxy = {"v": (0, 1), "^": (0, -1), "<": (-1, 0), ">": (1, 0)}
    d_ds = {"v": ("<", ">"), "^": ("<", ">"), "<": ("^", "v"), ">": ("^", "v")}

    while queue:
        src, srcio, x, y, d, dist = queue.pop(0)
        dx, dy = d_dxy[d]
        if grid[y + dy][x + dx] == ".":
            queue.append((src, srcio, x + dx, y + dy, d, dist + 1))
        elif (x + dx, y + dy) in entrances:
            ent, inout = entrances[x + dx, y + dy]
            dists[src, srcio, ent, inout] = dist
            if (ent, ("outer" if inout == "inner" else "inner")) in exited:
                continue
            ex, ey, ed, eio = [
                e for e in portals[ent] if e[0] != x + dx and e[1] != y + dy
            ][0]
            # print(f"{ent} from {x+dx},{y+dy},{srcio} to {ex},{ey},{ed},{eio}")
            exited.add((ent, ("outer" if inout == "inner" else "inner")))
            queue.append((ent, eio, ex, ey, ed, 0))
        for d_ in d_ds[d]:
            dx_, dy_ = d_dxy[d_]
            if grid[y + dy_][x + dx_] == ".":
                queue.append((src, srcio, x + dx_, y + dy_, d_, dist + 1))
            elif (x + dx_, y + dy_) in entrances:
                ent, inout = entrances[x + dx_, y + dy_]
                dists[src, srcio, ent, inout] = dist
                if (ent, ("outer" if inout == "inner" else "inner")) in exited:
                    continue
                ex, ey, ed, eio = [
                    e for e in portals[ent] if e[0] != x + dx_ and e[1] != y + dy_
                ][0]
                # print(f"{ent} from {x+dx_},{y+dy_},{srcio} to {ex},{ey},{ed},{eio}")
                exited.add((ent, ("outer" if inout == "inner" else "inner")))
                queue.append((ent, eio, ex, ey, ed, 0))

    # part 1

    graph = {}
    for (n1, n1io, n2, n2io), d in dists.items():
        graph[n1] = graph.get(n1, set())
        graph[n1].add((n2, d))
        graph[n2] = graph.get(n2, set())
        graph[n2].add((n1, d))

    distances = {}
    distances["AA"] = 0
    q = ["AA"]
    infty = 10**20
    for v in graph:
        if v != "AA":
            distances[v] = infty
            q.append(v)
    visited = set()
    while q:
        v = min(q, key=lambda k: distances[k])
        q.remove(v)
        visited.add(v)
        for n, d in graph[v]:
            if n in visited:
                continue
            alt = distances[v] + d
            if alt < distances[n]:
                distances[n] = alt
    print(distances["ZZ"] - 1)

    # part 2

    graph = {}
    for (n1, n1io, n2, n2io), d in dists.items():
        graph[n1, n1io] = graph.get((n1, n1io), set())
        graph[n1, n1io].add((n2, n2io, d))
        graph[n2, n2io] = graph.get((n2, n2io), set())
        graph[n2, n2io].add((n1, n1io, d))

    # print(graph)

    queue = [("AA", "outer", 0, 0)]

    seen = {}
    while queue:
        # print(queue)
        c, cio, level, steps = queue.pop(0)
        seen[c, cio, level] = steps
        if c == "ZZ":
            print(steps - 1)
            break

        for n, nio, d in graph[(c, cio)]:
            if level == 0 and nio == "outer" and n != "ZZ":
                continue
            if level > 0 and n in ["AA", "ZZ"]:
                continue
            nio_ = "inner" if nio == "outer" else "outer"
            level_ = level + 1 if nio == "inner" else level - 1
            if (n, nio_, level_) not in seen:
                queue.append(
                    (
                        n,
                        nio_,
                        level_,
                        steps + d,
                    )
                )
