#!/usr/bin/env python3

def insertionsort(items: list):
    for i in range(len(items)):
        for j in range(i - 1, -1, -1):
            if items[j] < items[j + 1]:
                break
            items[j], items[j + 1] = items[j + 1], items[j]

