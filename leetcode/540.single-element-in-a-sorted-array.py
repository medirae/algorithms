# Category: algorithms
# Level: Medium
# Percent: 59.341328%



# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
# 
# Return the single element that appears only once.
# 
# Your solution must run in O(log n) time and O(1) space.
# 
#  
# Example 1:
# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:
# Input: nums = [3,3,7,7,10,11,11]
# Output: 10
# 
#  
# Constraints:
# 
# 
# 	1 <= nums.length <= 10⁵
# 	0 <= nums[i] <= 10⁵
# 
 

# CODE-START
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        if nums[0] != nums[1]:
            return nums[0]
        
        if nums[-1] != nums[-2]:
            return nums[-1]

        l, r = 0, n - 1
        while l <= r:
            m = l + (r - l) // 2
            ls = int(nums[m] == nums[m + 1])
            rs = int(nums[m] == nums[m - 1])
            if not ls and not rs:
                return nums[m]

            if (r - m - ls) & 1:
                l = m + 1 + ls
            else:
                r = m - 1 - rs
# CODE-END
