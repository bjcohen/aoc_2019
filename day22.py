import re


if __name__ == "__main__":
    with open("day22.txt") as f:
        instrs = [l.strip() for l in f]

    deck = list(range(10007))
    for i in instrs:
        if i == "deal into new stack":
            deck.reverse()
        elif m := re.match(r"deal with increment (\d+)", i):
            n = int(m[1])
            j = 0
            deck_ = [None for _ in range(len(deck))]
            for j, c in enumerate(deck):
                deck_[j * n % len(deck)] = c
            deck = deck_
        elif m := re.match(r"cut (-?\d+)", i):
            n = int(m[1])
            deck = deck[n:] + deck[:n]
    print(deck.index(2019))

    n = 2020
    niter = 101741582076661
    ncards = 119315717514047
    a, b = 1, 0
    for i in instrs:
        if i == "deal into new stack":
            a, b = -a % ncards, (ncards - 1 - b) % ncards
        elif m := re.match(r"deal with increment (\d+)", i):
            c = int(m[1])
            a, b = a * c % ncards, b * c % ncards
        elif m := re.match(r"cut (-?\d+)", i):
            c = int(m[1])
            a, b = a, (b - c) % ncards
    r = b * pow(1 - a, ncards - 2, ncards)
    print(((n - r) * pow(a, niter * (ncards - 2), ncards) + r) % ncards)
