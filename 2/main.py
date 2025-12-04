from common import run


def main(inp: str) -> int:
    data = inp.split(",")
    print(f"{len(data)} sets in data")

    ret = 0
    for line in data:
        # Split into ranges
        split = line.split("-")
        low, high = split[0], split[1]
        print(f"\n{low=} {high=}")

        # For a given start range identify smallest next repeat
        seen = set()
        for repeats in range(2, len(high) + 1):
            n_digits_low = len(low)
            if n_digits_low % repeats == 0:
                prefix = int(low[:(n_digits_low // repeats)])
            else:
                prefix = 10 ** (n_digits_low // repeats)

            full_val = int(''.join([str(prefix) * repeats]))
            while full_val <= int(high):
                if (full_val >= int(low)) and (full_val not in seen):
                    print(f"Found invalid {full_val=}")
                    ret += full_val
                    seen.add(full_val)
                prefix += 1
                full_val = int(''.join([str(prefix) * repeats]))

    return ret


if __name__ == "__main__":
    run(main)