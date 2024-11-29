if __name__ == "__main__":
    lo, hi = 156218, 652527
    count = 0
    for i in range(lo, hi + 1):
        istr = str(i)
        if (
            len(istr) == 6
            and all(istr[i + 1] >= istr[i] for i in range(5))
            and any(istr[i + 1] == istr[i] for i in range(5))
        ):
            count += 1
    print(count)
    count = 0
    for i in range(lo, hi + 1):
        istr = str(i)
        if (
            len(istr) == 6
            and all(istr[i + 1] >= istr[i] for i in range(5))
            and any(
                istr[i + 1] == istr[i]
                and (i == 4 or istr[i + 2] != istr[i + 1])
                and (i == 0 or istr[i - 1] != istr[i])
                for i in range(5)
            )
        ):
            count += 1
    print(count)
