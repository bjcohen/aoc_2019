def fuel(m):
    if m <= 8:
        return 0
    f = m // 3 - 2
    return f + fuel(f)


if __name__ == "__main__":
    with open("day1.txt") as f:
        print(sum(int(l) // 3 - 2 for l in f))
    with open("day1.txt") as f:
        print(sum(fuel(int(l)) for l in f))
