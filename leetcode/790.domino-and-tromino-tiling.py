# Category: algorithms
# Level: Medium
# Percent: 51.299347%



# You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.
# 
# Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 10⁹ + 7.
# 
# In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.
# 
#  
# Example 1:
# 
# Input: n = 3
# Output: 5
# Explanation: The five different ways are shown above.
# 
# 
# Example 2:
# 
# Input: n = 1
# Output: 1
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= n <= 1000
# 
 

# CODE-START
class Solution:
    def numTilings(self, n: int) -> int:
        # f[n] = f[n - 1] + f[n - 2] + p[n - 1]  f[0] = 0, f[1] = 1, f[2] = 2 for every n > 2
        # p[n] = p[n - 1] + 2*f[n - 2]           p[0] = 0, p[1] = 0, p[2] = 2
        #
        # f[n] = 2*f[n - 1] + f[n - 3] ?
        #
        # proof:
        # presume: f[n] = f[n-1] + f[n-2] + p[n-1] and p[n] = p[n-1] + 2*f[n-2]
        # f[n] = f[n-1] + f[n-2] + p[n-1]
        # f[n] = f[n-1] + f[n-2] + p[n-2] + 2*f[n-3] # expansion
        # 
        # f[n-1] = f[n-2] + f[n-3] + p[n-2]
        # f[n-1] = f[n-2] + f[n-3] + p[n-3] + 2*f[n-4] # expansion
        # 
        # # replace p[n-2] in f[n-1] from f[n]
        # f[n-1] = f[n-2] + f[n-3] + (f[n] - f[n-1] - f[n-2] - 2*f[n-3])
        # f[n] = f[n-1] - f[n-2] - f[n-3] + f[n-1] + f[n-2] + 2*f[n-3]
        # f[n] = 2*f[n - 1] + f[n - 3]           f[0] = 0, f[1] = 1, f[2] = 2 for every n > 2
        # 
        # tada!

        mod = 10 ** 9 + 7
        f0, f1, f2 = 0, 1, 1
        for _ in range(1, n):
            f0, f1, f2 = f1, f2, (2*f2 + f0) % mod
        
        return f2

        # vd: vertical domino: size=1
        # hd: horizontal domino: size=2
        # # inverse tromino: 0 <= extension: size=3 + 2 * extension
        # u_it: up inverse tromino: (0)size=3
        # d_it: up inverse tromino: (0)size=3
        # # same side tromino: 0 <= extension: size=4 + 2 * extension
        # u_sst: up same side tromino: size=4
        # d_sst: down same side tromino: size=4

        blocks = {
            'vd': 1, 'hd': 2,
            'u_it': 3, 'd_it': 3,
            'u_sst': 4, 'd_sst': 4,
        }
        extends = {'u_it', 'd_it', 'u_sst', 'd_sst'}
        combos = 0
        def bt(remaining_size):
            rs = remaining_size
            if rs == 0:
                nonlocal combos
                combos += 1
                return
            
            for block, size in blocks.items():
                if size > rs:
                    break
                if block not in extends:
                    bt(rs - size)
                else:
                    for ext in range((rs - size) // 2 + 1):
                        bt(rs - size - 2 * ext)

        bt(n)
        return combos
        
# CODE-END
