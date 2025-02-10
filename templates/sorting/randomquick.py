#!/usr/bin/env python3

from random import randint

def randomquicksort(items: list, lower: int = -1, upper: int = -1):
    if lower == -1:
        lower = 0
    if upper == -1:
        upper = len(items) - 1

    if upper - lower + 1 <= 1:
        return

    pivot = randint(lower, upper)
    items[lower], items[pivot] = items[pivot], items[lower]
    pivot = lower

    itr = pivot + 1
    candidate = pivot + 1
    while itr <= upper:
        lucky = randint(0, 1)
        if items[itr] < items[pivot] or (items[itr] == items[pivot] and lucky):
            items[itr], items[candidate] = items[candidate], items[itr]
            candidate += 1
        itr += 1

    items[candidate - 1], items[pivot] = items[pivot], items[candidate - 1]
    pivot = candidate - 1

    if pivot - 1 > lower:
        randomquicksort(items, lower, pivot - 1)
    if pivot + 1 < upper:
        randomquicksort(items, pivot + 1, upper)
