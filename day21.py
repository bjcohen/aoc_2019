import intcode

if __name__ == "__main__":
    with open("day21.txt") as f:
        prog = intcode.parse(f)

    def not_(a, b):
        return [ord("N"), ord("O"), ord("T"), 32, a, 32, b, 10]

    def and_(a, b):
        return [ord("A"), ord("N"), ord("D"), 32, a, 32, b, 10]

    def or_(a, b):
        return [ord("O"), ord("R"), 32, a, 32, b, 10]

    def walk():
        return [ord(c) for c in "WALK"] + [10]

    def run():
        return [ord(c) for c in "RUN"] + [10]

    A = ord("A")
    B = ord("B")
    C = ord("C")
    D = ord("D")
    E = ord("E")
    F = ord("F")
    G = ord("G")
    H = ord("H")
    I = ord("I")
    T = ord("T")
    J = ord("J")

    hull_damage = intcode.run(
        prog,
        iter(
            not_(B, T)
            + and_(C, T)
            + or_(T, J)
            + not_(A, T)
            + or_(T, J)
            + not_(C, T)
            + and_(D, T)
            + or_(T, J)
            + walk(),
        ),
    )
    outputs = [hd for hd in hull_damage]
    print("".join(chr(c) for c in outputs if c < 0x110000))
    print([c for c in outputs if c >= 0x110000][0])

    hull_damage = intcode.run(
        prog,
        iter(
            not_(B, T)
            + and_(C, T)
            + and_(D, T)
            + or_(T, J)
            + not_(A, T)
            + or_(T, J)
            + not_(C, T)
            + and_(D, T)
            + and_(H, T)
            + or_(T, J)
            + run(),
        ),
    )
    outputs = [hd for hd in hull_damage]
    print("".join(chr(c) for c in outputs if c < 0x110000))
    print([c for c in outputs if c >= 0x110000][0])
