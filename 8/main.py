from common import run


def get_dist(x, y):
    return (x[0] - y[0])**2 + (x[1] - y[1])**2 + (x[2] - y[2])**2

def main(inp: str):
    data = [
        tuple(int(x) for x in line.split(','))
        for line in inp.splitlines()
    ]
    N = len(data)

    # Get top n_closest connections
    connections = []

    for i in range(N):
        for j in range(i + 1, N):
            dist = get_dist(data[i], data[j])
            connections.append((dist, (i, j)))
    connections.sort()

    # Make connections, track connected components, size of three largest components
    roots = dict()
    nodes = dict()
    largest = 0
    for conn in connections:
        _, (i, j) = conn

        if (i not in nodes) and (j not in nodes):
            # Create a new pair
            head = min(i, j)
            roots[head] = [i, j]
            nodes[i] = head
            nodes[j] = head
        elif (i not in nodes):
            # Merge i into j
            head = nodes[j]
            nodes[i] = head
            roots[head].append(i)
        elif (j not in nodes):
            # Merge j into i
            head = nodes[i]
            nodes[j] = head
            roots[head].append(j)
        else:
            # Merge the two elements
            if nodes[i] == nodes[j]:
                # If were already in the same component nothing to do
                head = nodes[i]
            else:
                head = min(nodes[i], nodes[j])
                nothead = max(nodes[i], nodes[j])
                to_merge = roots.pop(nothead)
                for k in to_merge:
                    nodes[k] = head
                roots[head].extend(to_merge)
        
        # Check if weve connected all
        largest = max(largest, len(roots[head]))
        if largest == len(data):
            # Answer is product of x components
            return data[i][0] * data[j][0]

    # If were here the algorithm fails
    return -1

if __name__ == "__main__":
    run(main)
