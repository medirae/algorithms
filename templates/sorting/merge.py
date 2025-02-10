#!/usr/bin/env python3

def merge(items: list, start: int, mid: int, end: int):
    leftp = start
    rightp = mid + 1

    if items[mid] <= items[mid + 1]:
        return

    while leftp <= mid and rightp <= end:
        if items[leftp] <= items[rightp]:
            leftp += 1
            continue

        # move items to right by 1 element
        value = items[rightp]
        index = rightp
        while index > leftp:
            items[index] = items[index - 1]
            index -= 1
        items[leftp] = value
        
        leftp += 1
        rightp += 1
        # this is crucial to reflect the fact that one
        #  element was moved to the left portion, therefore
        #  the size of the left portion increased by one,
        #  pushing the midline 1 element to the right.
        mid += 1

def mergesort(items: list, lower: int = -1, upper: int = -1):
    if lower == -1:
        lower = 0
    if upper == -1:
        upper = len(items) - 1
    if upper - lower + 1 == 2:
        items[lower], items[upper] = \
                min(items[lower], items[upper]), \
                max(items[lower], items[upper])
        return
    elif lower >= upper:
        return
    
    # same as (lower + upper) // 2, but prevents overflow
    print(lower, upper)
    print(items[lower:upper])
    mid = lower + (upper - lower) // 2
    mergesort(items, lower, mid)
    mergesort(items, mid + 1, upper)
    merge(items, lower, mid, upper)
    print(items)
