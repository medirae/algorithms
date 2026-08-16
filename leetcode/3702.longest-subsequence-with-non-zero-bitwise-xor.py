# Category: algorithms
# Level: Medium
# Percent: 37.53911%



# You are given an integer array nums.
# 
# Return the length of the longest subsequence in nums whose bitwise XOR is non-zero. If no such subsequence exists, return 0.
# 
#  
# Example 1:
# 
# 
# Input: nums = [1,2,3]
# 
# Output: 2
# 
# Explanation:
# 
# One longest subsequence is [2, 3]. The bitwise XOR is computed as 2 XOR 3 = 1, which is non-zero.
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,3,4]
# 
# Output: 3
# 
# Explanation:
# 
# The longest subsequence is [2, 3, 4]. The bitwise XOR is computed as 2 XOR 3 XOR 4 = 5, which is non-zero.
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= nums.length <= 10⁵
# 	0 <= nums[i] <= 10⁹
# 
 

# CODE-START
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        if [0] * len(nums) == nums:
            return 0

        x = 0
        for n in nums:
            x ^= n

        if x != 0:
            return len(nums)

        return len(nums) - 1
        
# CODE-END
