# Category: algorithms
# Level: Hard
# Percent: 68.05904%



# You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).
# 
# It starts raining, and water gradually rises over time. At time t, the water level is t, meaning any cell with elevation less than equal to t is submerged or reachable.
# 
# You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.
# 
# Return the minimum time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).
# 
#  
# Example 1:
# 
# Input: grid = [[0,2],[1,3]]
# Output: 3
# Explanation:
# At time 0, you are in grid location (0, 0).
# You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
# You cannot reach point (1, 1) until time 3.
# When the depth of water is 3, we can swim anywhere inside the grid.
# 
# 
# Example 2:
# 
# Input: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
# Output: 16
# Explanation: The final route is shown.
# We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
# 
# 
#  
# Constraints:
# 
# 
# 	n == grid.length
# 	n == grid[i].length
# 	1 <= n <= 50
# 	0 <= grid[i][j] < n²
# 	Each value grid[i][j] is unique.
# 
 

# CODE-START
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        return self.greedy_dijkstra(grid)
        return self.binary_search(grid)
        return self.union_find(grid)

    @staticmethod
    def union_find(grid):
        n = len(grid)
        u = list(range(n ** 2))
        v = [[False] * n for _ in range(n)]
        p = [None] * (n ** 2) # reverse index
        for i in range(n):
            for j in range(n):
                p[grid[i][j]] = (i, j)

        for t in range(n ** 2):
            i, j = p[t]
            v[i][j] = True
            
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if (
                    0 <= (x := i + dx) < n and
                    0 <= (y := j + dy) < n and
                    v[x][y]
                ):
                    rij = n * i + j
                    while rij != u[rij]:
                        u[rij] = u[u[rij]]
                        rij = u[rij]
                    
                    rxy = n * x + y
                    while rxy != u[rxy]:
                        u[rxy] = u[u[rxy]]
                        rxy = u[rxy]
                    
                    if rij != rxy:
                        u[rij] = rxy

            r0 = 0
            while r0 != u[r0]:
                u[r0] = u[u[r0]]
                r0 = u[r0]
            
            rn = n ** 2 - 1
            while rn != u[rn]:
                u[rn] = u[u[rn]]
                rn = u[rn]

            if r0 == rn:
                return t

    @staticmethod
    def binary_search(grid):
        n = len(grid)
        
        def dfs(i, j, v, t):
            if (i, j) == (n - 1, n - 1):
                return True
            
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if (
                    0 <= (x := i + dx) < n and
                    0 <= (y := j + dy) < n and
                    v[x][y] and
                    grid[x][y] <= t
                ):
                    v[x][y] = False
                    if dfs(x, y, v, t):
                        return True
            
            return False

        l, r = max(grid[0][0], grid[n - 1][n - 1]), n ** 2 - 1
        while l < r:
            t = l + (r - l) // 2

            v = [[True] * n for _ in range(n)]
            v[0][0] = False
            if dfs(0, 0, v, t):
                r = t
            else:
                l = t + 1

        return r

    @staticmethod
    def greedy_dijkstra(grid):
        n, n2 = len(grid), len(grid) ** 2
        h = [(grid[0][0], 0, 0)]
        grid[0][0] = n2
        m = 0
        while h:
            t, j, i = heapq.heappop(h)
            i, j = -i, -j

            m = max(m, t)
            if (i, j) == (n - 1, n - 1):
                return m

            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                if (
                    0 <= (x := i + dx) < n and
                    0 <= (y := j + dy) < n and 
                    grid[x][y] != n2
                ):
                    heapq.heappush(h, (grid[x][y], -y, -x))
                    grid[x][y] = n2
        
# CODE-END
