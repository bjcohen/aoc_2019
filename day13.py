import intcode

if __name__ == "__main__":
    with open("day13.txt") as f:
        prog = intcode.parse(f)
    outputs = [o for o in intcode.run(prog, None)]
    tiles = []
    for i in range(len(outputs) // 3):
        [x, y, tid] = outputs[3 * i : 3 * i + 3]
        tiles.append((x, y, tid))
    print(sum(1 for t in tiles if t[2] == 2))
    prog[0] = 2

    def g():
        producer = None
        while True:
            if producer is None:
                x = yield
            else:
                x = yield producer()
            if x is not None:
                producer = x

    inputs = g()
    next(inputs)
    ic = intcode.run(prog, inputs)
    b = None
    p = None
    tiles = {}
    done = False
    score = None
    while not done:
        x, y, tid = None, None, None
        while x != -1:
            try:
                x, y, tid = next(ic), next(ic), next(ic)
            except StopIteration:
                done = True
                break
            tiles[(x, y)] = tid
            if tid == 4:
                b = x, y
            if tid == 3:
                p = x, y
        if tid is not None:
            score = tid

        def producer():
            if b[0] > p[0]:
                pi = 1
            elif b[0] < p[0]:
                pi = -1
            else:
                pi = 0
            return pi

        inputs.send(producer)
    print(score)
