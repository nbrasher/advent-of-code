from collections import defaultdict, deque
from copy import deepcopy
import re

from common import run


def find_paths(start, end, fwd, order):
    begin_tracking = False
    paths = defaultdict(int)
    paths[start] = 1
    for i in range(len(order) - 1, -1, -1):
        if order[i] == start:
            begin_tracking = True
        if begin_tracking:
            node = order[i]
            for e in fwd[node]:
                paths[e] += paths[node]
        if order[i] == end:
            break

    return paths[end]

def main(inp: str) -> int:
    # Build DAG edges forward and in reverse - i.e. you: {bbb, ccc}
    fwd = defaultdict(set)
    rev = defaultdict(set)
    for line in inp.splitlines():
        root = line.split(':')[0]
        edges = re.findall(r'\s([\w]{3})', line)
        fwd[root] = set(edges)
        for e in edges:
            rev[e].add(root)

    # Linearize the DAG in reverse order
    fwdcopy = deepcopy(fwd)
    seen = set()
    q = deque(['out'])
    order = ['out']
    while q:
        sink = q.pop()
        print(f"linearizing {sink}")
        for be in rev[sink]:
            if be not in seen:
                fwdcopy[be].remove(sink)
                if len(fwdcopy[be]) == 0:
                    q.appendleft(be)
                    order.append(be)
                    seen.add(be)

    return (
        find_paths('svr', 'fft', fwd, order) 
        * find_paths('fft', 'dac', fwd, order) 
        * find_paths('dac', 'out', fwd, order)
    ) + (
        find_paths('svr', 'dac', fwd, order) 
        * find_paths('dac', 'fft', fwd, order) 
        * find_paths('fft', 'out', fwd, order)    
    )

if __name__ == "__main__":
    run(main)
