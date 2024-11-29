def parse(f):
    return [int(i) for i in f.read().strip().split(",")]


def _parse2(prog, i, label=""):
    in_p1, in_p2, out_p = prog[i + 1 : i + 4]
    in_m1, in_m2 = prog[i] // 100 % 10, prog[i] // 1000 % 10
    assert prog[i] // 10000 % 10 == 0, f"prog[i] dest mode is immediate in {label}"
    in1 = in_p1 if in_m1 == 1 else prog[in_p1]
    in2 = in_p2 if in_m2 == 1 else prog[in_p2]
    return in1, in2, out_p


def _parse0(prog, i):
    p = prog[i + 1]
    m = prog[i] // 100 % 10
    return p if m == 1 else prog[p]


def run(prog, inputs, label=""):
    prog = prog.copy()
    i = 0
    outputs = []
    while (op := prog[i] % 100) != 99:
        if op == 1:
            in1, in2, out_p = _parse2(prog, i, label)
            prog[out_p] = in1 + in2
            i += 4
        elif op == 2:
            in1, in2, out_p = _parse2(prog, i, label)
            prog[out_p] = in1 * in2
            i += 4
        elif op == 3:
            assert prog[i] // 100 % 10 == 0, f"prog[i] mode is immediate in {label}"
            p = p = prog[i + 1]
            prog[p] = next(inputs)
            assert prog[p] is not None, f"prog[p] is none in {label}"
            i += 2
        elif op == 4:
            in_ = _parse0(prog, i)
            yield in_
            i += 2
        elif op == 5:
            in1, in2, _ = _parse2(prog, i, label)
            if in1 != 0:
                i = in2
            else:
                i += 3
        elif op == 6:
            in1, in2, _ = _parse2(prog, i, label)
            if in1 == 0:
                i = in2
            else:
                i += 3
        elif op == 7:
            in1, in2, out_p = _parse2(prog, i, label)
            prog[out_p] = 1 if in1 < in2 else 0
            i += 4
        elif op == 8:
            in1, in2, out_p = _parse2(prog, i, label)
            prog[out_p] = 1 if in1 == in2 else 0
            i += 4
        else:
            raise Exception(f"unhandled op=[{op}] at i=[{i}]")
