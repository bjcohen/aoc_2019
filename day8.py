if __name__ == "__main__":
    w = 25
    h = 6
    wh = w * h
    with open("day8.txt") as f:
        pixels = f.read().strip()
    assert len(pixels) % wh == 0
    min_zeroes = wh
    for i in range(len(pixels) // wh):
        num_zeroes = sum(1 for p in pixels[i * wh : i * wh + wh] if p == "0")
        if num_zeroes < min_zeroes:
            min_zeroes = num_zeroes
            num_ones = sum(1 for p in pixels[i * wh : i * wh + wh] if p == "1")
            num_twos = sum(1 for p in pixels[i * wh : i * wh + wh] if p == "2")

    print(num_ones * num_twos)

    result = ""

    for i in range(h):
        for j in range(w):
            c = None
            for l in range(len(pixels) // wh):
                p = pixels[l * wh + w * i + j]
                if p in ["0", "1"]:
                    c = p
                    break
            result += c
        result += "\n"
    print(result)
