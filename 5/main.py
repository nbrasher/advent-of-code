from typing import List, Tuple

from common import run


def part1(ranges: List[Tuple[int, int]], ingredients: List[int]) -> int:
    # Iterate through ranges to get count of fresh ingredients
    ret = 0
    for i in ingredients:
        spoiled = True
        for rng in ranges:
            if rng[0] <= i <= rng[1]:
                spoiled = False
                break
        
        ret += int(not spoiled)
    return ret


def part2(ranges: List[Tuple[int, int]]) -> int:
    # Sort by start date
    N = len(ranges)
    ranges.sort()

    # Greedily combine subsequent ranges into new list of ranges
    deduped = []
    prev = ranges[0]
    for i in range(1, N):
        # If no overlap, append
        cur = ranges[i]
        if prev[1] < cur[0]:
            deduped.append(prev)
            prev = cur
        # If some overlap update
        else:
            prev = (min(prev[0], cur[0]), max(prev[1], cur[1]))
            # If this is our last interval append anyways
            if i == (N - 1):
                deduped.append(prev)
        
    # Get full count from de-duplicated list
    ret = 0
    for rng in deduped:
        ret += (rng[1] - rng[0] + 1)

    return ret


def main(inp: str):
    # Parse into ranges and ingredients
    data = inp.splitlines()
    n_ranges = data.index('')
    
    ranges = []
    for i in range(n_ranges):
        rng = data[i].split('-')
        ranges.append((int(rng[0]), int(rng[1])))
    ingredients = [int(x) for x in data[n_ranges + 1:]]

    return part2(ranges)

if __name__ == "__main__":
    run(main)
