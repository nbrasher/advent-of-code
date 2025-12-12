from collections import Counter
import re

from common import run


def main(inp: str) -> int:
    dims = []
    # Get shape sizes
    data = inp.splitlines()
    i = 0
    shape_sizes = []
    while i < len(data):
        if re.match(r'\d\:', data[i]):
            size = 0
            for j in range(1, 4):
                c = Counter(data[i + j])
                size += c['#']
            i += 3
            shape_sizes.append(size)
        i += 1

    # Get grid dimensions
    for line in inp.splitlines():
        dim_x_y = re.findall(r'(\d+)x(\d+)\:', line)
        if dim_x_y:
            dim = [tuple(int(x) for x in dim_x_y[0])]
            numbers = re.findall(r'\s(\d+)', line)
            # Total of all shapes needed
            dim.append(tuple(int(x) for x in numbers))
            dims.append(dim)

    ret = 0
    # Turns out all we need is to determine the easiest cases, where there are
    # enough 3x3 tiles to avoid packing, or where there arent enough spaces
    # regardless of packing efficiency
    for dim in dims:
        tiles_x = dim[0][0] // 3
        tiles_y = dim[0][1] // 3
        total_units_avail = (dim[0][0] * dim[0][1])
        total_units_needed = sum(x * y for x, y in zip(shape_sizes, dim[1]))

        if sum(dim[1]) <= (tiles_x * tiles_y):
            print("No packing needed")
            ret += 1
        elif total_units_needed > total_units_avail:
            print("Packing impossible")
        else:
            print("PACKING ALGO NEEDED")

    return ret

if __name__ == "__main__":
    run(main)
