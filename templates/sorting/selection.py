#!/usr/bin/env python3

def selectionsort(items: list):
    for i in range(len(items) - 1):
        min_value = float('inf')
        min_index = i
        for j in range(i, len(items)):
            if items[j] < min_value:
                min_value = items[j]
                min_index = j

        if min_index == i:
            continue
        items[i], items[min_index] = items[min_index], items[i]

