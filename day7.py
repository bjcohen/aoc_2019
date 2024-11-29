import intcode
from itertools import chain

if __name__ == "__main__":
    with open("day7.txt") as f:
        prog = intcode.parse(f)
    max_output = -1
    for a in range(5):
        for b in range(5):
            for c in range(5):
                for d in range(5):
                    for e in range(5):
                        if len({a, b, c, d, e}) != 5:
                            continue
                        oa = intcode.run(prog, iter([a, 0]))
                        ob = intcode.run(prog, chain([b], oa))
                        oc = intcode.run(prog, chain([c], ob))
                        od = intcode.run(prog, chain([d], oc))
                        oe = intcode.run(prog, chain([e], od))
                        max_output = max(next(oe), max_output)
    print(max_output)
    max_output = -1
    for a in range(5, 10):
        for b in range(5, 10):
            for c in range(5, 10):
                for d in range(5, 10):
                    for e in range(5, 10):
                        if len({a, b, c, d, e}) != 5:
                            continue

                        def gen_in_a():
                            queue = [a, 0]
                            while True:
                                x = yield queue[0]
                                if x is None:
                                    queue.pop(0)
                                else:
                                    queue.append(x)

                        in_a = gen_in_a()
                        oa = intcode.run(prog, in_a, "a")
                        ob = intcode.run(prog, chain([b], oa), "b")
                        oc = intcode.run(prog, chain([c], ob), "c")
                        od = intcode.run(prog, chain([d], oc), "d")
                        oe = intcode.run(prog, chain([e], od), "e")
                        while True:
                            try:
                                oe_val = next(oe)
                                in_a.send(oe_val)
                            except StopIteration:
                                max_output = max(oe_val, max_output)
                                break
    print(max_output)
