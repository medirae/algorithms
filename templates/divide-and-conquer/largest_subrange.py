#!/usr/bin/env python3

from random import randint

def sweep(items: list, start: int, stop: int) -> tuple[int]:
    if start < stop:
        indexes = range(start, stop + 1)
    else:
        indexes = range(start, stop - 1, -1)
    
    sums, maximum = 0, float('-inf')
    begin, end = start, stop
    for i in indexes:
        sums += items[i]
        if sums > maximum:
            maximum = sums
            end = i
    
    begin, end = min((begin, end)), max((begin, end))
    return maximum, begin, end


def largest_subrange(items: list,
                     maximum: int = float('-inf'),
                     begin: int = -1,
                     end: int = -1,
                     lower: int = -1,
                     upper: int = -1):
    """
    the largest subrange found among any of the function calls:
        maximum: length
        begin: start index in items
        end: end index in items (inclusive)
    """
    if lower == -1:
        lower = 0
    if upper == -1:
        upper = len(items) - 1
    
    mid = lower + (upper - lower) // 2

    r_max, r_begin, r_end = sweep(items, mid + 1, upper)
    l_max, l_begin, l_end = sweep(items, mid, lower)

    if r_max >= maximum:
        begin, end = r_begin, r_end
        maximum = r_max
    if l_max >= maximum:
        begin, end = l_begin, l_end
        maximum = l_max
    if r_max + l_max >= maximum:
        begin, end = l_begin, r_end
        maximum = l_max + r_max
    
    if upper - lower + 1 <= 4:
        return maximum, begin, end

    r_max, r_begin, r_end = largest_subrange(items, maximum, begin, end, mid + 1, upper)
    l_max, l_begin, l_end = largest_subrange(items, maximum, begin, end, lower, mid)

    if r_max >= maximum:
        begin, end = r_begin, r_end
        maximum = r_max
    if l_max >= maximum:
        begin, end = l_begin, l_end
        maximum = l_max
    
    return maximum, begin, end

def largest_subrange_brute(items: list):
    maximum = float('-inf')
    for i in range(len(items)):
        sums = 0
        for j in range(i, len(items)):
            sums += items[j]
            maximum = max(sums, maximum)
    
    return maximum

def generate_list(n: int = 0, lower: int = 0, upper: int = 0):
    if not n:
        n = randint(10, 50)
    if not lower:
        lower = randint(0, 100)
    if not upper:
        upper = randint(0, 100)

    lower, upper = min((lower, upper)), max((lower, upper))

    return [randint(lower, upper) for i in range(n)]

def test():
    for _ in range(10):
        items = generate_list()
        l1, l2 = largest_subrange(items), largest_subrange_brute(items)
        assert l1[0] == l2, 'sum is wrong!'
