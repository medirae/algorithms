# Category: algorithms
# Level: Medium
# Percent: 43.173485%



# You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.
# 
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:
# 
# 
# 	0 <= j <= nums[i] and
# 	i + j < n
# 
# 
# Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.
# 
#  
# Example 1:
# 
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# 
# Example 2:
# 
# Input: nums = [2,3,0,1,4]
# Output: 2
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= nums.length <= 10⁴
# 	0 <= nums[i] <= 1000
# 	It's guaranteed that you can reach nums[n - 1].
# 
 

# CODE-START
class Solution:
    def jump(self, nums: List[int]) -> int:
        return self.greedy_bfs(nums)
        return self.dp2d(nums)

    @staticmethod
    def greedy_bfs(nums):
        n = len(nums)
        cr = nr = 0  # reach
        j = 0
        for i in range(n - 1):
            r = i + nums[i]
            if r > nr:
                nr = r
            if nr >= n - 1:
                return j + 1
            if i == cr:
                j += 1
                cr = nr
        
        return j

    @staticmethod
    def dp2d(nums):
        n = len(nums)
        dp = [[(float("inf") if i != j else 0) for j in range(n)] for i in range(n)]

        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if nums[j] >= i - j:
                    dp[i][j] = 1
                elif nums[j] != 0 and j < i - 1:
                    print(f'dp[{i}][{j}]')
                    for k in range(i - 1, j, -1):
                        print(f'\tdp[{i}][{k}] + dp[{k}][{j}] = {dp[i][k] + dp[k][j]}')
                    dp[i][j] = min(dp[i][k] + dp[k][j] for k in range(j + 1, j + nums[j] + 1))

        return dp[n - 1][0]
        
# CODE-END
