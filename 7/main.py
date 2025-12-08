from common import run


def main(inp: str):
    data = inp.splitlines()

    M, N = len(data), len(data[0])
    prev = [(0 if data[0][i] != 'S' else 1) for i in range(N)]
    cur = [0 for _ in range(N)]

    for i in range(1, M):
        for j in range(N):
            if data[i][j] == '^':
                cur[j - 1] += prev[j]
                cur[j + 1] += prev[j]
            else:
                cur[j] += prev[j]
        # Reset prev, cur
        prev = cur.copy()
        cur = [0 for _ in range(N)]

    return sum(prev)

if __name__ == "__main__":
    run(main)
