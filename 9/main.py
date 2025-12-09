from common import run


def check_intersect(p1, p2, horizontal, vertical):
    min_x, max_x = p1[0], p2[0]
    if min_x > max_x:
        min_x, max_x = max_x, min_x
    min_y, max_y = p1[1], p2[1]
    if min_y > max_y:
        min_y, max_y = max_y, min_y

    for h in horizontal:
        yval, (seg_start, seg_end) = h
        if (min_y < yval < max_y):
            if not ((seg_end <= min_x) or (seg_start >= max_x)):
                # print(f"Found conflict with {p1} {p2} and horizontal edge {h}")
                return True
    for v in vertical:
        xval, (seg_start, seg_end) = v
        if (min_x < xval < max_x):
            if not ((seg_end <= min_y) or (seg_start >= max_y)):
                # print(f"Found conflict with {p1} {p2} and vertical edge {v}")
                return True
    return False

def main(inp: str):
    data = [
        tuple(int(x) for x in line.split(','))
        for i, line in enumerate(inp.splitlines())
    ]
    N = len(data)
    ordered_plus = data.copy()
    ordered_plus.sort(key = lambda x: x[0] + x[1])
    ordered_minus = data.copy()
    ordered_minus.sort(key = lambda x: x[0] - x[1])

    ret = 0
    # Iterate through edge pairs and build vertical and horizontal edges
    horizontal = []
    vertical = []
    for i in range(N):
        j = (i + 1) % N
        if data[i][0] == data[j][0]:
            edge = [data[i][1], data[j][1]]
            edge.sort()
            vertical.append((data[i][0], tuple(edge)))
        else:
            edge = [data[i][0], data[j][0]]
            edge.sort()
            horizontal.append((data[i][1], tuple(edge)))

    for i in range(N):
        prv = (i - 1) % N
        nxt = (i + 1) % N
        point1 = data[i]

        top_left = (data[nxt][1] <= data[i][1]) and (data[prv][0] <= data[i][0]) and (data[prv][0] < data[nxt][0])
        bottom_left = (data[nxt][0] <= data[i][0]) and (data[prv][1] >= data[i][1]) and (data[prv][0] > data[nxt][0])

        # For top left, check increasing x + y
        if top_left:
            # print(f"{data[i]} is a top-left corner")
            for j in range(N):
                point2 = ordered_plus[j]
                if (point2[0] + point2[1]) > (point1[0] + point1[1]):
                    if not check_intersect(point1, point2, horizontal, vertical):
                        area = ((point2[1] - point1[1]) + 1) * ((point2[0] - point1[0]) + 1)
                        # print(f"Found valid rectangle {point1} {point2} {area=}")
                        ret = max(ret, area)
        # For bottom left, check increasing x - y
        elif bottom_left:
            # print(f"{data[i]} is bottom-left")
            for j in range(N):
                point2 = ordered_minus[j]
                if (point2[0] - point2[1]) > (point1[0] - point1[1]):
                    if not check_intersect(point1, point2, horizontal, vertical):
                        area = ((point1[1] - point2[1]) + 1) * ((point2[0] - point1[0]) + 1)
                        # print(f"Found valid rectangle {point1} {point2} {area=}")
                        ret = max(ret, area)

    return ret

if __name__ == "__main__":
    run(main)
