import intcode


if __name__ == "__main__":
    with open("day23.txt") as f:
        prog = intcode.parse(f)

    natx, naty = None, None

    def cb(i):
        global natx, naty
        computers = yield
        while True:
            dest = yield
            x = yield
            y = yield
            if dest == 255:
                if naty is None:
                    print(y)
                natx, naty = x, y
                continue
            computers[dest].send(x)
            computers[dest].send(y)

    callbacks = [cb(i) for i in range(50)]
    computers = [
        intcode.run(prog, callback, str(i), sync_out=True, sync_in=False)
        for i, callback in enumerate(callbacks)
    ]
    for callback in callbacks:
        callback.send(None)
        callback.send(computers)
    for i, c in enumerate(computers):
        next(c)
        c.send(i)
    last_natx, last_naty = None, None
    while True:
        for c in computers:
            c.send(-1)
        if last_natx == natx and last_naty == naty:
            print(naty)
            break
        last_natx, last_naty = natx, naty
        computers[0].send(natx)
        computers[0].send(naty)
