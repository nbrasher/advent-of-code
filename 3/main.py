from common import run
from functools import lru_cache

@lru_cache(maxsize=None)
def largest_subset(s: str, ix: int, length: int) -> int:
    n = len(s)
    max_val = 0
    if length == 1:
        return int(max(s[ix:]))
    
    max_most_sig_digit = 0
    for i in range(n - length, ix - 1, -1):
        if int(s[i]) >= max_most_sig_digit:
            max_sub_int = largest_subset(s, i + 1, length - 1)
            max_most_sig_digit = int(s[i])
            max_val = 10 ** (length - 1) * max_most_sig_digit + max_sub_int
    
    return max_val


def main(inp: str):
    data = inp.splitlines()

    ret = 0
    for line in data:
        max_val = largest_subset(line, 0, 12)
        ret += max_val
        print(f"{line} {max_val=}")

    return ret

if __name__ == "__main__":
    run(main)