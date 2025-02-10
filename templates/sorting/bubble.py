#!/usr/bin/env python3

def bubblesort(items: list):
    n = len(items)
    for i in range(n):
        for j in range(n - i - 1):
            if items[j + 1] < items[j]:
                items[j], items[j + 1] = items[j + 1], items[j]
