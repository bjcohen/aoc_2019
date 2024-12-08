if __name__ == "__main__":
    with open("day24.txt") as f:
        grid = [[c for c in row.strip()] for row in f]
    grids = []
    while True:
        if grid in grids:
            break
        grids.append(grid)
        grid_ = [["." for _ in row] for row in grid]
        for j, row in enumerate(grid):
            for i, c in enumerate(row):
                n_adj = 0
                if i > 0 and row[i - 1] == "#":
                    n_adj += 1
                if i < len(row) - 1 and row[i + 1] == "#":
                    n_adj += 1
                if j > 0 and grid[j - 1][i] == "#":
                    n_adj += 1
                if j < len(grid) - 1 and grid[j + 1][i] == "#":
                    n_adj += 1
                if c == "#" and n_adj == 1:
                    grid_[j][i] = "#"
                if c == "." and n_adj in [1, 2]:
                    grid_[j][i] = "#"
        grid = grid_
    print(
        sum(
            sum(pow(2, i + j * len(grid[0])) for i, c in enumerate(row) if c == "#")
            for j, row in enumerate(grid)
        )
    )

    grids = grids[:1]
    for i in range(200):
        grids.insert(0, [["." for _ in row] for row in grids[0]])
        grids.append([["." for _ in row] for row in grids[0]])
        grids_ = [[["." for _ in row] for row in grid] for grid in grids]
        for j, grid in enumerate(grids):
            for y, row in enumerate(grid):
                for x, c in enumerate(row):
                    if (x, y) == (2, 2):
                        continue
                    n_adj = 0
                    if x > 0 and row[x - 1] == "#":
                        n_adj += 1
                    if x < 4 and row[x + 1] == "#":
                        n_adj += 1
                    if y > 0 and grid[y - 1][x] == "#":
                        n_adj += 1
                    if y < 4 and grid[y + 1][x] == "#":
                        n_adj += 1
                    if x == 0 and j > 0 and grids[j - 1][2][1] == "#":
                        n_adj += 1
                    if x == 4 and j > 0 and grids[j - 1][2][3] == "#":
                        n_adj += 1
                    if y == 0 and j > 0 and grids[j - 1][1][2] == "#":
                        n_adj += 1
                    if y == 4 and j > 0 and grids[j - 1][3][2] == "#":
                        n_adj += 1
                    if (x, y) == (2, 1) and j < len(grids) - 1:
                        n_adj += sum(1 for g in grids[j + 1][0] if g == "#")
                    if (x, y) == (2, 3) and j < len(grids) - 1:
                        n_adj += sum(1 for g in grids[j + 1][4] if g == "#")
                    if (x, y) == (1, 2) and j < len(grids) - 1:
                        n_adj += sum(1 for y_ in range(5) if grids[j + 1][y_][0] == "#")
                    if (x, y) == (3, 2) and j < len(grids) - 1:
                        n_adj += sum(1 for y_ in range(5) if grids[j + 1][y_][4] == "#")
                    if c == "#" and n_adj == 1:
                        grids_[j][y][x] = "#"
                    if c == "." and n_adj in [1, 2]:
                        grids_[j][y][x] = "#"
        # print(sum(sum(sum(1 for c in row if c == "#") for row in grid) for grid in grids))
        grids = grids_
    # print(
    #     "\n\n".join(
    #         f"Grid {i-len(grids)//2}\n" + "\n".join("".join(row) for row in grid)
    #         for i, grid in enumerate(grids)
    #     ),
    #     "\n\n",
    # )
    # print(
    #     "\n\n".join(
    #         f"Grid {i-len(grids)//2}\n" + "\n".join("".join(row) for row in grid)
    #         for i, grid in enumerate(grids_)
    #     ),
    #     "\n\n",
    # )
    print(sum(sum(sum(1 for c in row if c == "#") for row in grid) for grid in grids))
