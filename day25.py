from collections.abc import Generator
import itertools
import re

import intcode

if __name__ == "__main__":
    with open("day25.txt") as f:
        prog = intcode.parse(f)

    class Actor(Generator):
        def __init__(self):
            self.in_buf = ""
            self.out_buf = ""
            self.ic = None
            self.path = []
            self.seen = set()
            self.doors = []
            self.items = []
            self.holding = []
            self.dropped = []
            self.room = None
            self.combination = None
            self.combinations = None

        def throw(self, type=None, value=None, traceback=None):
            raise StopIteration

        def send(self, c):
            self.in_buf += chr(c)
            print(chr(c), end="")
            if self.in_buf.endswith("Command?\n"):
                m = re.search(r"== ([\w ]+) ==", self.in_buf)
                if m:
                    self.room = m[1]
                if self.room == "Security Checkpoint" and len(self.holding) == 8:
                    if self.combinations is None:
                        self.combinations = itertools.chain.from_iterable(
                            itertools.combinations(self.holding, r)
                            for r in range(len(self.holding) + 1)
                        )
                    if self.combination is None:
                        self.combination = next(self.combinations)
                    print("drop combination", self.combination)
                    for item in self.holding:
                        if item in self.combination and item not in self.dropped:
                            print(f"drop {item}")
                            self.out_buf += f"drop {item}\n"
                            self.dropped.append(item)
                            break
                        elif item not in self.combination and item in self.dropped:
                            print(f"take {item}")
                            self.out_buf += f"take {item}\n"
                            self.dropped.remove(item)
                            break
                    else:
                        self.combination = None
                        print("north")
                        self.out_buf += "north\n"
                    return
                things = re.findall(r"- ([\w ]+)\n", self.in_buf)
                if things:
                    self.doors = [
                        t for t in things if t in ["east", "south", "west", "north"]
                    ]
                    self.items = [
                        t for t in things if t not in ["east", "south", "west", "north"]
                    ]
                if self.items:
                    print(self.items)
                    item = self.items.pop()
                    if item in [
                        "astronaut ice cream",
                        "food ration",
                        "fixed point",
                        "polygon",
                        "asterisk",
                        "dark matter",
                        "weather machine",
                        "easter egg",
                    ]:
                        print("take " + item)
                        self.out_buf += "take " + item + "\n"
                        self.in_buf = ""
                        self.holding.append(item)
                        self.path = []
                        self.seen = set()
                        return
                cands = []
                for d in self.doors:
                    if (
                        (d == "east" and (self.room, d) not in self.seen)
                        or (d == "south" and (self.room, d) not in self.seen)
                        or (d == "west" and (self.room, d) not in self.seen)
                        or (d == "north" and (self.room, d) not in self.seen)
                    ):
                        cands.append(d)
                print(
                    self.doors,
                    cands,
                    tuple(sorted(self.holding)),
                    self.path,
                )
                if len(cands) > 0:
                    n = cands[0]
                    self.path.append(n)
                elif self.path:
                    if self.path[-1] == "east":
                        n = "west"
                    elif self.path[-1] == "south":
                        n = "north"
                    elif self.path[-1] == "west":
                        n = "east"
                    elif self.path[-1] == "north":
                        n = "south"
                    self.path.pop()
                else:
                    raise StopIteration
                print(n)
                self.out_buf += n + "\n"
                self.seen.add((self.room, n))
                self.in_buf = ""

        def __next__(self):
            if self.out_buf:
                c = self.out_buf[0]
                self.out_buf = self.out_buf[1:]
                return ord(c)

    a = Actor()
    ic = intcode.run(prog, a, sync_in=True, sync_out=True)
    try:
        next(ic)
    except StopIteration:
        pass
