import intcode
import itertools


if __name__ == "__main__":
    with open("day19.txt") as f:
        prog = intcode.parse(f)

    print(
        sum(
            next(intcode.run(prog, iter([i, j])))
            for i, j in itertools.product(range(50), repeat=2)
        )
    )

    n = 2000

    grid = []
    last_row_leading_edge = None
    last_row_trailing_edge = None
    for y in range(n):
        row = []
        grid.append(row)
        leading_edge = None
        trailing_edge = None
        for x in range(n):
            if (
                last_row_trailing_edge is not None
                and x < last_row_trailing_edge
                and row
                and row[-1] == "#"
            ):
                row.append("#")
            elif (
                (last_row_leading_edge is None or x >= last_row_leading_edge)
                and (leading_edge is None or row[-1] == "#")
                and next(intcode.run(prog, iter([x, y]))) == 1
            ):
                row.append("#")
                if leading_edge is None:
                    leading_edge = x
            else:
                row.append(".")
                if leading_edge is not None and trailing_edge is None:
                    trailing_edge = x
        if leading_edge is not None:
            last_row_leading_edge = leading_edge
        last_row_trailing_edge = trailing_edge

    for i in range(100):
        print("".join(grid[i][:100]))

    lf = 2
    found = {}

    for y in range(n):
        for x in range(n):
            if grid[y][x] != "#":
                continue
            if all(
                x + i < n
                and y + i < n
                and grid[y][x + i] == "#"
                and grid[y + i][x] == "#"
                for i in range(lf)
            ):
                found[lf] = (x, y)
                lf += 1

    print(max(found))
    x100, y100 = found[100]
    print(10000 * x100 + y100)
