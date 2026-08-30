# Category: algorithms
# Level: Medium
# Percent: 61.64456%



# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
# 
# The solution set must not contain duplicate subsets. Return the solution in any order.
# 
#  
# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Example 2:
# Input: nums = [0]
# Output: [[],[0]]
# 
#  
# Constraints:
# 
# 
# 	1 <= nums.length <= 10
# 	-10 <= nums[i] <= 10
# 
 

# CODE-START
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        c = Counter(nums)
        nums, n = [k for k in c], len(c)
        dp = [None] * n
        def bt(ndx=0):
            if ndx == n:
                return [[]]

            if dp[ndx] is None:
                dp[ndx] = bt(ndx + 1) + [
                    [nums[ndx]] * nc + i for i in bt(ndx + 1)
                    for nc in range(1, c[nums[ndx]] + 1)
                ]
                
            return dp[ndx]
        
        return bt()
        
# CODE-END
