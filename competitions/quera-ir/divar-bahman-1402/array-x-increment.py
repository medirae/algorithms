#!/usr/bin/env python3

from typing import *

def min_steps(n, x, arr):
    from math import ceil
    def check_non_decreasing(array):
        for ndx in range(len(array) - 1):
            if array[ndx + 1] < array[ndx]:
                return False
        return True
    
    if n < 2:
        return 0
    if x < 1:
        return -1
    if check_non_decreasing(arr):
        return 0

    steps = 0
    start = 1
    while not check_non_decreasing(arr):
        minimum = float('inf')
        value = float('-inf')    
        for ndx in range(start - 1, n - 1):
            if arr[ndx + 1] < arr[ndx]:  # non-dec element
                start = ndx + 1
                value = arr[ndx]
                break
        for ndx in range(start, n):
            minimum = min(minimum, arr[ndx])
        increment = ceil((value - minimum) / x)
        for ndx in range(start, n):
            arr[ndx] += increment * x
        steps += increment

    return steps

def brute(arr):
    pass

def test():
    tests = [
        [2, 2, [-3, 3]],
        [4, 1, [-2, -4, 4, -3]],
        [3, 0, [-73, -4, -5]],
        [1, 3, [1]]
    ]
    for t in tests:
        print(t)
        s = min_steps(*t)
        print(f's: {s}\n')

def get_input():
    q = int(input().strip())
    tests = list()
    for _ in range(q):
        n, x = list(map(int, input().strip().split(' ')))
        arr = list(map(int, input().strip().split(' ')))
        tests.append([n, x, arr])

    return tests

if __name__ == '__main__':
    # test()
    pass

for t in get_input():
    print(min_steps(*t))