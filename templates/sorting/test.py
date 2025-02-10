#!/usr/bin/env python3

from random import shuffle, randint

def generate_list(n: int = 0, lower: int = 0, upper: int = 0):
    if not n:
        n = randint(10, 50)
    if not lower:
        lower = randint(0, 100)
    if not upper:
        upper = randint(0, 100)

    lower, upper = min((lower, upper)), max((lower, upper))

    return [randint(lower, upper) for i in range(n)]

def sort(*args):
    ## import and use your sort function here
    from heaparray import heapsort
    return heapsort(*args)

items = generate_list(10, 1, 20)
answer = sorted(items[:])
items = sort(items)
assert type(items) == type(answer), 'not the same type'
assert len(items) == len(answer), 'not the same length'
assert items == answer, "not the same values"
