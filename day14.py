import graphlib


def solve(n):
    targets = {"FUEL": n}
    sorter = graphlib.TopologicalSorter()
    for output, (_, inputs) in formulas.items():
        sorter.add(output, *[i[1] for i in inputs])
    order = [n for n in sorter.static_order()]
    for t in reversed(order):
        if t == "ORE":
            continue
        n = targets[t]
        del targets[t]
        no, inputs = formulas[t]
        nf = n // no
        if n % no != 0:
            nf += 1
        for ni, input_ in inputs:
            targets[input_] = targets.get(input_, 0) + ni * nf
    return targets["ORE"]


if __name__ == "__main__":
    with open("day14.txt") as f:
        formulas = {}
        for r in f:
            parts = r.strip().split(" => ")
            inputs = [
                (int(p[0]), p[1]) for p in (p.split(" ") for p in parts[0].split(", "))
            ]
            output_parts = parts[1].split(" ")
            formulas[output_parts[1]] = (int(output_parts[0]), inputs)
    print(solve(1))

    one_t = 1_000_000_000_000

    lo, hi = 0, 1 << 30
    while True:
        midpoint = lo + (hi - lo) // 2
        solve_midpoint = solve(midpoint)
        if solve_midpoint > one_t:
            if hi - lo <= 1:
                ans = hi
                break
            hi = midpoint
        elif solve_midpoint <= one_t:
            if hi - lo <= 1:
                ans = lo
                break
            lo = midpoint
    print(ans)
