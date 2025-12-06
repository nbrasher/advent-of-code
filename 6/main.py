import re
from copy import deepcopy

from common import run


def main(inp: str):
    # Parse inputs
    data = inp.splitlines()
    operators = re.sub(r'\s+', ' ', data[-1]).split(' ')

    # Get lines as strings, transpose with row coordinate running backwards
    operands = []
    group = []
    for i in range(len(data[0])):
        digit = ""
        for j in range(len(data) - 2, -1, -1):
            digit += data[j][i]
        digit = digit.strip()
        if digit != "":
            group.append(int(digit[::-1]))
        else:
            operands.append(deepcopy(group))
            group = []
    operands.append(group)

    ret = 0
    for i in range(len(operators)):
        ans = 0
        if operators[i] == "*":
            ans = 1
        for j in range(len(operands[i])):
            if operators[i] == "*":
                ans = ans * int(operands[i][j])
            else:
                ans += int(operands[i][j])
        
        ret += ans

    return ret

if __name__ == "__main__":
    run(main)
