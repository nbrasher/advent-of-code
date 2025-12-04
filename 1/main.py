from common import run


def day_1(inp: str) -> int:
    data = inp.splitlines()
    print(f"{len(data)} lines in data")

    ret = 0
    loc = 50
    for line in data:
        direction = line[0]
        val = int(line[1:])

        if direction == "R":
            ret += (loc + val) // 100
            loc = (loc + val) % 100
        else:
            ret += ((-loc % 100) + val) // 100
            loc = (loc - val) % 100

        # print(f"{line=} {loc=} {ret=}")

    return ret


if __name__ == "__main__":
    run(day_1)