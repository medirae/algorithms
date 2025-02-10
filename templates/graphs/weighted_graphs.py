#!/usr/bin/env python3

from dataclasses import dataclass, field
from typing import Any
from adjacency_list import EdgeNode, AdjLGraph

def prim(g: AdjLGraph, start: int) -> int:
    """
    i
    p
    intree[MAXV+1]
    distance[MAXV+1]
    v
    w
    dist
    weight
    """
    dist = float('inf')
    weight = 0
    intree = [False] * g.nvertices
    distance = [float('inf')] * g.nvertices
    parent = [-1] * g.nvertices
    
    distance[start] = 0
    v = start
    while not intree[v]:
        intree[v] = True
        if v != start:
            print(f'edge ({parent[v]}, {v}) in tree')
            weight += dist
        p = g.edges[v]
        while p is not None:
            w = p.y
            if distance[w] > p.weight and not intree[w]:
                distance[w] = p.weight
                parent[w] = v
            p = p.next
        
        dist = float('inf')
        for i in range(g.nvertices):
            if not intree[i] and dist > distance[i]:
                dist = distance[i]
                v = i
    
    return weight

def test_prim(text):
    g = AdjLGraph()
    n = int(text.strip().split(' ')[0])
    g.init(n, False)
    g.read(text)
    g.print_graph(g)

    o = prim(g, 0)
    print(o)

if __name__ == '__main__':
    text = """
    11 13
    0 1 1
    0 4 2
    1 2 3
    1 3 4
    1 4 5
    2 3 6
    3 4 7
    5 6 1
    5 7 2
    6 8 3
    7 8 4
    7 9 5
    8 10 6
    """
    test_prim(text)