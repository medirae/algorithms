# Category: algorithms
# Level: Medium
# Percent: 59.698254%



# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# 
#  
# Example 1:
# 
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
# 
# 
# Example 2:
# 
# Input: nums = [0,1,0,3,2,3]
# Output: 4
# 
# 
# Example 3:
# 
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= nums.length <= 2500
# 	-10⁴ <= nums[i] <= 10⁴
# 
# 
#  
# Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
 

# CODE-START
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.binary_search(nums)
        return self.dp(nums)
        return self.bf_backtracking(nums)

    @staticmethod
    def binary_search(nums):
        s = list()
        for v in nums:
            i = bisect_left(s, v)
            if i == len(s):
                s.append(v)
            else:
                s[i] = v
            
        return len(s)

    @staticmethod
    def dp(nums):
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)

    @staticmethod
    def bf_backtracking(nums):
        n = len(nums)
        picked = list()
        def bt(ndx=0):
            m = len(picked)
            for i in range(ndx, n):
                if not picked or nums[i] > picked[-1]:
                    picked.append(nums[i])
                    if (v := bt(i)) > m:
                        m = v
                    picked.pop()
            
            return m

        return bt()
        
# CODE-END
