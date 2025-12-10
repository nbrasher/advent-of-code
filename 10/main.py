from collections import deque
import re

from common import run

import numpy as np
from scipy.optimize import milp, LinearConstraint


def part_one(target, moves, weights) -> int:
    # Cast as graph search using BFS for shortest path
    start = tuple([False for _ in range(len(target))])
    seen = {start}
    q = deque([(0, start)])

    while q:
        dist, node = q.pop()
        if node == target:
            return dist
        
        for move in moves:
            new_node = list(node)
            for neighbor in list(move):
                new_node[neighbor] = not new_node[neighbor]
            new_node = tuple(new_node)
            if new_node not in seen:
                seen.add(new_node)
                q.appendleft((dist + 1, new_node))

    # If were here algorithm failed
    raise ValueError("Unable to find a path")

def part_two(init, moves, target) -> int:
    # Re-cast as ILP
    dim = len(target)
    n_el = len(moves)
    c = np.ones(n_el)
    integrality = np.ones(n_el)
    target = np.array(target)
    bounds_matrix = [
        [int(i in move) for i in range(dim)]
        for move in moves
    ]
    bounds_matrix = np.array(bounds_matrix).T

    constraints = LinearConstraint(bounds_matrix, target, target)
    res = milp(c=c, constraints=constraints, integrality=integrality)

    ans = bounds_matrix @ res.x
    assert np.allclose(ans, target), f"Incorrect answer {ans=} {target=}"
    assert all(i >= 0 for i in res.x), f"Negative values found {res.x}"

    # The np.round is needed here otherwise 121.999999999 -> 121
    return int(np.round(res.x.sum()))

def main(inp: str) -> int:
    target_arr = []
    moves_arr = []
    weights_arr = []
    for line in inp.splitlines():
        g = re.findall(r'\[(.*)\]', line)
        target = tuple([x == '#' for x in g[0]])
        target_arr.append(target)

        g = re.findall(r'\(([\d\,]+)\)', line)
        moves = [tuple([int(x) for x in tup.split(',')]) for tup in g]
        moves_arr.append(moves)

        g = re.findall(r'\{([\d\,]+)\}', line)
        weights = [int(x) for x in g[0].split(',')]
        weights_arr.append(weights)

    ret = [
        part_two(target, moves, weights)
        for target, moves, weights in zip(target_arr, moves_arr, weights_arr)
    ]
    return sum(ret)

if __name__ == "__main__":
    run(main)
