# Category: algorithms
# Level: Medium
# Percent: 82.57952%



# Given an integer array nums of unique elements, return all possible subsets (the power set).
# 
# The solution set must not contain duplicate subsets. Return the solution in any order.
# 
#  
# Example 1:
# 
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# 
# 
# Example 2:
# 
# Input: nums = [0]
# Output: [[],[0]]
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= nums.length <= 10
# 	-10 <= nums[i] <= 10
# 	All the numbers of nums are unique.
# 
 

# CODE-START
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        dp = [None] * (n + 1)
        def bt(ndx=0, p=False):
            if ndx == n:
                return [[]]

            if dp[ndx] is None:
                dp[ndx] = bt(ndx + 1, False) + [[nums[ndx]] + i for i in bt(ndx + 1, True)]

            return dp[ndx]

        return bt()
        
# CODE-END
