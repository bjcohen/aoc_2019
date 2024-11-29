def parse(f):
    return [int(i) for i in f.read().strip().split(",")]


def _resolve_val(prog, p, m, rel_base):
    if m == 0:
        _check_addr(prog, p)
        return prog[p]
    elif m == 1:
        return p
    elif m == 2:
        return prog[rel_base + p]
    else:
        assert False, f"unhandled mode [{m}]"


def _resolve_ptr(prog, p, m, rel_base):
    if m == 0:
        return p
    elif m == 1:
        assert False, "can't resolve an address in immediate mode"
    elif m == 2:
        return rel_base + p
    else:
        assert False, f"unhandled mode [{m}]"


def _parse2(prog, i, rel_base, label):
    in_p1, in_p2, out_p = prog[i + 1 : i + 4]
    in_m1, in_m2 = prog[i] // 100 % 10, prog[i] // 1000 % 10
    out_m = prog[i] // 10000 % 10
    in1 = _resolve_val(prog, in_p1, in_m1, rel_base)
    in2 = _resolve_val(prog, in_p2, in_m2, rel_base)
    out_p = _resolve_ptr(prog, out_p, out_m, rel_base)
    return in1, in2, out_p


def _parse0ptr(prog, i, rel_base, label):
    p = prog[i + 1]
    m = prog[i] // 100 % 10
    return _resolve_ptr(prog, p, m, rel_base)


def _parse0val(prog, i, rel_base, label):
    p = prog[i + 1]
    m = prog[i] // 100 % 10
    return _resolve_val(prog, p, m, rel_base)


def _check_addr(prog, p):
    if p >= len(prog):
        prog.extend(0 for _ in range(p - len(prog) + 1))


def run(prog, inputs, label="unlabeled"):
    prog = prog.copy()
    i = 0
    outputs = []
    rel_base = 0
    while (op := prog[i] % 100) != 99:
        if op == 1:
            in1, in2, out_p = _parse2(prog, i, rel_base, label)
            _check_addr(prog, out_p)
            prog[out_p] = in1 + in2
            i += 4
        elif op == 2:
            in1, in2, out_p = _parse2(prog, i, rel_base, label)
            _check_addr(prog, out_p)
            prog[out_p] = in1 * in2
            i += 4
        elif op == 3:
            out_p = _parse0ptr(prog, i, rel_base, label)
            _check_addr(prog, out_p)
            prog[out_p] = next(inputs)
            assert prog[out_p] is not None, f"prog[p] is none in {label}"
            i += 2
        elif op == 4:
            in_ = _parse0val(prog, i, rel_base, label)
            yield in_
            i += 2
        elif op == 5:
            in1, in2, _ = _parse2(prog, i, rel_base, label)
            if in1 != 0:
                i = in2
            else:
                i += 3
        elif op == 6:
            in1, in2, _ = _parse2(prog, i, rel_base, label)
            if in1 == 0:
                i = in2
            else:
                i += 3
        elif op == 7:
            in1, in2, out_p = _parse2(prog, i, rel_base, label)
            _check_addr(prog, out_p)
            prog[out_p] = 1 if in1 < in2 else 0
            i += 4
        elif op == 8:
            in1, in2, out_p = _parse2(prog, i, rel_base, label)
            _check_addr(prog, out_p)
            prog[out_p] = 1 if in1 == in2 else 0
            i += 4
        elif op == 9:
            in_ = _parse0val(prog, i, rel_base, label)
            rel_base += in_
            i += 2
        else:
            raise Exception(f"unhandled op=[{op}] at i=[{i}]")
