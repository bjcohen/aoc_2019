import math


if __name__ == "__main__":
    with open("day16.txt") as f:
        signal = [int(c) for c in f.read().strip()]
    signal1 = signal.copy()
    for _ in range(100):
        signal1_ = []
        for i, x in enumerate(signal1):
            pattern = [0] * (i + 1) + [1] * (i + 1) + [0] * (i + 1) + [-1] * (i + 1)
            signal1_.append(
                abs(
                    sum(
                        s * pattern[(j + 1) % len(pattern)]
                        for j, s in enumerate(signal1)
                    )
                )
                % 10
            )
        signal1 = signal1_
    print("".join(str(s) for s in signal1[:8]))
    signal2 = signal.copy() * 5000
    for _ in range(100):
        signal2_ = []
        half_sum = sum(signal2)
        for i, x in enumerate(signal2):
            signal2_.append(half_sum % 10)
            half_sum -= signal2[i]
        signal2 = signal2_
    offset = int("".join(str(s) for s in signal[:7]))
    print(
        "".join(
            str(s)
            for s in signal2[
                offset - 5000 * len(signal) : 8 + offset - 5000 * len(signal)
            ]
        )
    )
