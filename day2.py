def solve(opcodes, x, y):
    opcodes = opcodes.copy()
    opcodes[1] = x
    opcodes[2] = y
    i = 0
    while (op := opcodes[i]) != 99:
        in1, in2 = opcodes[opcodes[i + 1]], opcodes[opcodes[i + 2]]
        out_p = opcodes[i + 3]
        if op == 1:
            opcodes[out_p] = in1 + in2
        elif op == 2:
            opcodes[out_p] = in1 * in2
        else:
            raise Exception(f'unhandled op: [{op}]')
        i += 4
    return opcodes[0]


if __name__ == '__main__':
    with open('day2.txt') as f:
        opcodes = [int(o) for o in f.read().strip().split(',')]

    print(solve(opcodes, 12, 2))

    for i in range(100):
        for j in range(100):
            if solve(opcodes, i, j) == 19690720:
                print(100 * i + j)
