#!/usr/bin/env python3
# https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/

from typing import *

class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        import heapq
        from collections import defaultdict, deque

        # second attempt: bfs + pq
        graph = defaultdict(lambda: defaultdict(lambda: float('inf')))
        for u, v, w in edges:
            if u == v:
                continue
            graph[u][v] = min(graph[u][v], w)
            graph[v][u] = min(graph[v][u], w)

        ans = [0] + [float('inf')] * (n - 1)
        pq = [(0, 0)]  # (time, node)
        visited = set()
        while pq:
            time, node = heapq.heappop(pq)
            if node in visited:
                continue
            visited.add(node)

            for target, weight in graph[node].items():
                if target in visited or time + weight >= disappear[target]:
                    continue

                if time + weight < ans[target]:
                    ans[target] = time + weight
                    heapq.heappush(pq, (ans[target], target))

        return [(-1 if a == float('inf') else a) for a in ans]

        # first attempt: bfs + q
        graph = defaultdict(lambda: defaultdict(lambda: float('inf')))
        for u, v, w in edges:
            if u == v:
                continue
            graph[u][v] = min(graph[u][v], w)
            graph[v][u] = min(graph[v][u], w)

        ans = [0] + [float('inf')] * (n - 1)
        q = deque([(0, 0)])
        visited = {0}
        while q:
            for _ in range(len(q)):
                node, time = q.popleft()
                ans[node] = min(ans[node], time)
                for target, weight in graph[node].items():
                    if (target in visited and weight + time >= ans[target]) or \
                        weight + time >= disappear[target]:
                        continue
                    q.append((target, time + weight))
                    visited.add(target)

        return [(-1 if a == float('inf') else a) for a in ans]

def test():
    tests = [
        [3,[[0,1,2],[1,2,1],[0,2,4]],[1,1,5]],
        [3,[[0,1,2],[1,2,1],[0,2,4]],[1,3,5]],
        [2,[[0,1,1]],[1,1]],
        [1,[[0,0,2],[0,0,2],[0,0,1],[0,0,3],[0,0,2],[0,0,4],[0,0,4]],[6]],
        [4,[[2,3,8],[2,0,9],[3,0,8],[2,1,6],[2,1,3]],[10,6,16,19]],
        [9,[[7,0,10],[0,1,4],[8,8,4],[1,6,1],[1,0,7],[8,4,9],[1,7,1],[1,0,10]],[6,15,20,10,7,11,5,14,13]],
        [7,[[6,1,10],[1,0,2],[3,0,10],[5,0,3],[2,0,10],[5,4,8],[5,4,3],[4,2,1],[2,2,7],[1,3,6]],[15,6,12,15,9,16,11]],
    ]
    for t in tests:
        print(*t)
        s = Solution().minimumTime(*t)
        print(f's: {s}\n')

if __name__ == '__main__':
    test()
