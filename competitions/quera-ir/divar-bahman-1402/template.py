#!/usr/bin/env python3

from typing import *

def eye2eye(arr1, arr2):
    pass

def brute(arr):
    pass

def test():
    tests = [
        [[1,1,0,1,0,0,1,1],
         [1,1,0,0,0,1,0,1]],
        [[0,0,0,1,1,1,0,1],
         [0,0,1,0,1,1,0,0]]
    ]
    for t in tests:
        print(t)
        s = eye2eye(*t)
        print(f's: {s}\n')

def get_input():
    arr1 = map(int, input().split(' '))
    arr2 = map(int, input().split(' '))
    return arr1, arr2

if __name__ == '__main__':
    test()
