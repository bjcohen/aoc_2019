def total_orbits(orbits, o, path=[]):
    if o not in orbits:
        return len(path)
    return sum(total_orbits(orbits, o_, path + [o]) for o_ in orbits[o]) + len(path)


def find_path(orbits, o, target, path=[]):
    if o == target:
        return path
    if o not in orbits:
        return None
    for o_ in orbits[o]:
        p = find_path(orbits, o_, target, path + [o])
        if p is not None:
            return p
    return None


def num_transfers(orbits):
    p1 = find_path(orbits, "COM", "YOU")
    p2 = find_path(orbits, "COM", "SAN")
    while p1[0] == p2[0]:
        p1 = p1[1:]
        p2 = p2[1:]
    return len(p1) + len(p2)


if __name__ == "__main__":
    with open("day6.txt") as f:
        orbits = {}
        for l in f:
            o0, o1 = l.strip().split(")")
            l = orbits.get(o0, [])
            orbits[o0] = l
            l.append(o1)
    print(total_orbits(orbits, "COM"))
    print(num_transfers(orbits))
