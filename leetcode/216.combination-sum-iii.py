# Category: algorithms
# Level: Medium
# Percent: 73.49753%



# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
# 
# 
# 	Only numbers 1 through 9 are used.
# 	Each number is used at most once.
# 
# 
# Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.
# 
#  
# Example 1:
# 
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Explanation:
# 1 + 2 + 4 = 7
# There are no other valid combinations.
# 
# Example 2:
# 
# Input: k = 3, n = 9
# Output: [[1,2,6],[1,3,5],[2,3,4]]
# Explanation:
# 1 + 2 + 6 = 9
# 1 + 3 + 5 = 9
# 2 + 3 + 4 = 9
# There are no other valid combinations.
# 
# 
# Example 3:
# 
# Input: k = 4, n = 1
# Output: []
# Explanation: There are no valid combinations.
# Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
# 
# 
#  
# Constraints:
# 
# 
# 	2 <= k <= 9
# 	1 <= n <= 60
# 
 

# CODE-START
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        summ = 0
        current = list()
        combs = list()

        # I think I overdid it lol

        @lru_cache
        def nsum(x):
            return (x * (x + 1)) // 2
        @lru_cache
        def range_sum(a, b):
            return nsum(max(a, b)) - nsum(min(a, b) - 1)
        @lru_cache
        def minsum(start, remaining):
            return range_sum(start, start + remaining - 1) # sum of remaining count of values from picked+1
        @lru_cache
        def maxsum(start, remaining):
            return range_sum(10 - remaining, 9) # sum of remaining count of values from 9 backwards
        def dfs(remaining: int):
            nonlocal summ
            if remaining == 0:
                if summ == n:
                    combs.append(current.copy())
                return

            rsumm = n - summ
            start = current[-1] + 1 if len(current) > 0 else 1            
            for pick in range(start, 11-remaining):
                if (rsumm < minsum(pick, remaining) or rsumm > maxsum(pick, remaining)):
                    continue
                current.append(pick)
                summ += pick
                dfs(remaining - 1)
                current.pop()
                summ -= pick
        
        dfs(k)
        return combs
        
# CODE-END
