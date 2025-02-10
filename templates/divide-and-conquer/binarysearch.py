#!/usr/bin/env python3

from random import randint

def binarysearch(items: list, value: int, lower: int = -1, upper: int = -1) -> int:
    if lower == -1:
        lower = 0
    if upper == -1:
        upper = len(items) - 1
    if upper < lower:
        return -1
    
    mid = lower + (upper - lower) // 2
    if items[mid] == value:
        return mid
    
    if   items[mid] < value:
        return binarysearch(items, value, mid + 1, upper)
    elif items[mid] > value:
        return binarysearch(items, value, lower, mid - 1)
    
def generate_list(n: int = 0, lower: int = 0, upper: int = 0):
    if not n:
        n = randint(10, 50)
    if not lower:
        lower = randint(0, 100)
    if not upper:
        upper = randint(0, 100)

    lower, upper = min((lower, upper)), max((lower, upper))

    return sorted([randint(lower, upper) for i in range(n)])

def test():
    items = generate_list(10, -10, 10)
    for item in items:
        index = binarysearch(items, item)
        assert index != -1, 'item was not found.'
        assert item == items[index]

if __name__ == '__main__':
    test()