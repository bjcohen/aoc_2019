def parse2(prog, i):
    in_p1, in_p2, out_p = prog[i + 1 : i + 4]
    in_m1, in_m2 = prog[i] // 100 % 10, prog[i] // 1000 % 10
    assert prog[i] // 10000 % 10 == 0
    in1 = in_p1 if in_m1 == 1 else prog[in_p1]
    in2 = in_p2 if in_m2 == 1 else prog[in_p2]
    return in1, in2, out_p


def parse0(prog, i):
    p = prog[i + 1]
    m = prog[i] // 100 % 10
    return p if m == 1 else prog[p]


def solve(prog, inputs):
    prog = prog.copy()
    inputs = inputs.copy()
    i = 0
    outputs = []
    while (op := prog[i] % 100) != 99:
        if op == 1:
            in1, in2, out_p = parse2(prog, i)
            prog[out_p] = in1 + in2
            i += 4
        elif op == 2:
            in1, in2, out_p = parse2(prog, i)
            prog[out_p] = in1 * in2
            i += 4
        elif op == 3:
            assert prog[i] // 100 % 10 == 0
            p = p = prog[i + 1]
            prog[p] = inputs.pop()
            i += 2
        elif op == 4:
            in_ = parse0(prog, i)
            outputs.append(in_)
            i += 2
        elif op == 5:
            in1, in2, _ = parse2(prog, i)
            if in1 != 0:
                i = in2
            else:
                i += 3
        elif op == 6:
            in1, in2, _ = parse2(prog, i)
            if in1 == 0:
                i = in2
            else:
                i += 3
        elif op == 7:
            in1, in2, out_p = parse2(prog, i)
            prog[out_p] = 1 if in1 < in2 else 0
            i += 4
        elif op == 8:
            in1, in2, out_p = parse2(prog, i)
            prog[out_p] = 1 if in1 == in2 else 0
            i += 4
        else:
            raise Exception(f'unhandled op=[{op}] at i=[{i}]')
    return outputs


if __name__ == '__main__':
    with open('day5.txt') as f:
        prog = [int(i) for i in f.read().strip().split(',')]
    outputs = solve(prog, [1])
    print(outputs[-1])
    outputs = solve(prog, [5])
    print(outputs[-1])
