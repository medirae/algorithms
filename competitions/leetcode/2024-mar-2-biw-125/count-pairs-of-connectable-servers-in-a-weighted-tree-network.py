#!/usr/bin/env python3
# https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network

from typing import *

class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        from collections import defaultdict, deque
        
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        n = max(graph.keys()) + 1
        paths = dict()
        for ndx in range(n):
            paths[ndx] = dict()
            q = deque([[ndx, 0, list()]])
            visited = {ndx}
            while q:
                node, summ, path = q.popleft()
                if summ % signalSpeed == 0:
                    paths[ndx][node] = path
                for edge, w in graph[node]:
                    if edge in visited:
                        continue
                    visited.add(edge)
                    q.append([edge, summ + w, path + [(node, edge)]])
        
        nums = [0] * n
        # for pndx1 in range(len(paths) - 1):
        #     for pndx2 in range(pndx1 + 1, len(paths)):
        #         if not paths[pndx1].intersection(paths[pndx2]):
        #             nums[ndx] += 1
        for k, v in paths.items():
            print(k, v)
        for start in range(n):
            for end in range(start + 1, n):
                count = 0
                for path_start, path_end in zip(paths[start].values(), paths[end].values()):
                    if not set(path_start) & set(path_end):
                        count += 1
                nums[start] += count
                nums[end] += count

        return nums

def test():
    tests = [
        [[[0,1,1],[1,2,5],[2,3,13],[3,4,9],[4,5,2]],1],
    ]
    for t in tests:
        print(*t)
        s = Solution().countPairsOfConnectableServers(*t)
        print(f's: {s}\n')

if __name__ == '__main__':
    test()
