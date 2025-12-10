import argparse
from time import time
from typing import Callable


def get_data(fn: str) -> str:
    with open(fn, 'r') as f:
        data = f.read()
    
    return data


def run(func: Callable):
    parser = argparse.ArgumentParser(description='Process some files.')
    parser.add_argument('filename', help='input file')
    args = parser.parse_args()

    start = time()
    data = get_data(args.filename)
    ans = func(data)
    end = time()
    print(f"Final answer {ans} took {1000*(end - start)}ms")