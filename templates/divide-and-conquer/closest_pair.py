#!/usr/bin/env python3

from math import sqrt
from random import randint

def distance(point1: tuple, point2: tuple) -> float:
    return round(sqrt((point2[1] - point1[1]) ** 2 + (point2[0] - point1[0]) ** 2), 3)

def closest_pair(points: list[tuple], lower: int = -1, upper: int = -1):
    if lower == -1:
        lower = 0
    if upper == -1:
        upper = len(points) - 1

    if   upper - lower + 1 == 2:
        d = distance(points[upper], points[lower])
        return d
    elif upper - lower + 1 <= 1:
        return float('inf')

    mid = lower + (upper - lower) // 2
    left = closest_pair(points, lower, mid)
    right = closest_pair(points, mid + 1, upper)
    midpoints = distance(points[mid + 1], points[mid])
    return min(left, right, midpoints)

def closest_pair_brute(points: list[tuple]):
    minimum = float('inf')
    for i in range(len(points)):
        for j in range(len(points)):
            if i <= j:
                continue
            d = distance(points[i], points[j])
            if d < minimum:
                minimum = d
    return minimum

def generate_list(n: int = 0, lower: int = 0, upper: int = 0):
    if not n:
        n = randint(10, 50)
    if not lower:
        lower = randint(0, 100)
    if not upper:
        upper = randint(0, 100)

    lower, upper = min((lower, upper)), max((lower, upper))

    return sorted([(randint(lower, upper), randint(lower, upper))
                   for i in range(n)], key=lambda x: (x[0], x[1]))

def test():
    for _ in range(20):
        points = generate_list()
        c1, c2 = closest_pair(points), closest_pair_brute(points)   
        assert c1 == c2, "didn't work!"
