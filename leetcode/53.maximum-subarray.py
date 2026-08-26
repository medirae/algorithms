# Category: algorithms
# Level: Medium
# Percent: 53.580494%



# Given an integer array nums, find the subarray with the largest sum, and return its sum.
# 
#  
# Example 1:
# 
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# 
# 
# Example 2:
# 
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# 
# 
# Example 3:
# 
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= nums.length <= 10⁵
# 	-10⁴ <= nums[i] <= 10⁴
# 
# 
#  
# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
 

# CODE-START
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.itr(nums)
        return self.dp(nums)
        return self.bf(nums)

    # TODO: divide and conquer

    @staticmethod
    def itr(nums):
        # kadane's algorithm
        n = len(nums)
        mp, mmp = 0, float('-inf')  # maximum picked, maximum of maximum picked
        for v in nums:
            mp = max(mp + v, v)
            if mp > mmp:
                mmp = mp
        
        return mmp

    @staticmethod
    def dp(nums):
        n = len(nums)
        dp = nums.copy()
        maximum = nums[n - 1]
        for ndx in range(n - 2, -1, -1):
            dp[ndx] = max(nums[ndx], nums[ndx] + dp[ndx + 1])
            if dp[ndx] > maximum:
                maximum = dp[ndx]
        
        return maximum

        dp = [[0] * n, [0] * n]
        dp[0][n - 1] = dp[1][n - 1] = nums[n - 1]
        for ndx in range(n - 2, -1, -1):
            dp[0][ndx] = max(nums[ndx] + dp[1][ndx + 1], dp[0][ndx + 1])
            dp[1][ndx] = max(nums[ndx] + dp[1][ndx + 1], nums[ndx])

        return dp[0][0]

    @staticmethod
    def bf(nums):
        n = len(nums)
        ninf = float('-inf')
        def bt(ndx=0, pick=False):
            if ndx == n:
                return 0 if pick else ninf

            return max(
                nums[ndx] + bt(ndx + 1, True),
                nums[ndx] if pick else bt(ndx + 1, False)
            )

        return bt()
        
# CODE-END
