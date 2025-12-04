from common import run

def main(inp: str):
    grid = [list(line) for line in inp.splitlines()]
    M, N = len(grid), len(grid[0])

    # Build an edge graph
    edges = dict()

    for i in range(M):
        for j in range(N):
            if grid[i][j] == '@':
                edgeset = set()
                for row in [-1, 0, 1]:
                    for col in [-1, 0, 1]:
                        if not (row == 0 and col == 0):
                            if (0 <= (i + row) < M) and (0 <= (j + col) < N):
                                if grid[i + row][j + col] == '@':
                                    edgeset.add((i + row, j + col))
                edges[(i, j)] = edgeset
    
    ret = 0
    # Iterate through making a remove list with count < 4    
    to_remove = [k for k, v in edges.items() if len(v) < 4]
    while len(to_remove) > 0:
        # Update edge counts by referencing original edge graph
        for i, j in to_remove:
            edgeset = edges.pop((i, j))
            for k, l in edgeset:
                edges[(k, l)].remove((i, j))

        ret += len(to_remove)
        to_remove = [k for k, v in edges.items() if len(v) < 4]
    
    # Halt when no more updates are made
    return ret

if __name__ == "__main__":
    run(main)