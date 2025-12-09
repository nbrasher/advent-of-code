from common import run


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
    # TODO - iterate through edge pairs and build vertical and horizontal edges
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
    # print(f"{horizontal=} {vertical=}")

    for i in range(N):
        prv = (i - 1) % N
        nxt = (i + 1) % N
        point1 = data[i]
        # TODO - for convex, top left, check increasing x + y
        if (data[prv][0] == data[i][0]) and (data[prv][1] > data[i][1]) and (data[nxt][0] > data[i][0]):
            # print(f"{i} is convex top-left")
            for j in range(N):
                point2 = ordered_plus[j]
                if (point2[0] + point2[1]) > (point1[0] + point1[1]):
                    intersect = False
                    for h in horizontal:
                        yval, (seg_start, seg_end) = h
                        if (point1[1] < yval < point2[1]):
                            if not ((seg_end <= point1[0]) or (seg_start >= point2[0])):
                                intersect = True
                                # print(f"Rectangle {point1} {point2} intersects with horizontal edge {h}")
                                break
                    for v in vertical:
                        xval, (seg_start, seg_end) = v
                        if (point1[0] < xval < point2[0]):
                            if not ((seg_end <= point1[1]) or (seg_start >= point2[1])):
                                intersect = True
                                # print(f"Rectangle {point1} {point2} intersects with vertical edge {v}")
                                break
                    if not intersect:
                        area = ((point2[1] - point1[1]) + 1) * ((point2[0] - point1[0]) + 1)
                        # print(f"Found valid rectangle {point1} {point2} {area=}")
                        ret = max(ret, area)
        # TODO - for convex bottom left, check increasing x - y
        elif (data[prv][1] == data[i][1]) and (data[prv][0] > data[i][0]) and (data[nxt][1] < data[i][1]):
            # print(f"{i} is convex bottom-left")
            for j in range(N):
                point2 = ordered_minus[j]
                if (point2[0] - point2[1]) > (point1[0] - point1[1]):
                    intersect = False
                    for h in horizontal:
                        yval, (seg_start, seg_end) = h
                        if (point2[1] < yval < point1[1]):
                            if not ((seg_end <= point1[0]) or (seg_start >= point2[0])):
                                intersect = True
                                # print(f"Rectangle {point1} {point2} intersects with horizontal edge {h}")
                                break
                    for v in vertical:
                        xval, (seg_start, seg_end) = v
                        if (point1[0] < xval < point2[0]):
                            if not ((seg_end <= point2[1]) or (seg_start >= point1[1])):
                                intersect = True
                                # print(f"Rectangle {point1} {point2} intersects with vertical edge {v}")
                                break
                    if not intersect:
                        area = ((point1[1] - point2[1]) + 1) * ((point2[0] - point1[0]) + 1)
                        # print(f"Found valid rectangle {point1} {point2} {area=}")
                        ret = max(ret, area)

    return ret

if __name__ == "__main__":
    run(main)
