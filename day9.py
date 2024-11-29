import intcode

if __name__ == "__main__":
    with open("day9.txt") as f:
        prog = intcode.parse(f)
    outputs = intcode.run(prog, iter([1]))
    print(next(outputs))
    outputs = intcode.run(prog, iter([2]))
    print(next(outputs))
