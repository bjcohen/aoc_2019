import intcode

if __name__ == "__main__":
    with open("day5.txt") as f:
        prog = intcode.parse(f)
    outputs = intcode.run(prog, iter([1]))
    print([o for o in outputs][-1])
    outputs = intcode.run(prog, iter([5]))
    print(next(outputs))
