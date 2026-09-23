# Category: algorithms
# Level: Medium
# Percent: 57.044197%



# Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
# 
#  
# Example 1:
# 
# Input: nums = [2,2,3,4]
# Output: 3
# Explanation: Valid combinations are: 
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
# 
# 
# Example 2:
# 
# Input: nums = [4,2,3,4]
# Output: 4
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= nums.length <= 1000
# 	0 <= nums[i] <= 1000
# 
 

# CODE-START
class Solution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums = sorted(x for x in nums if x)
        n = len(nums)

        rs = 2 + bisect_left(range(2, n), True, key=lambda x: (
            nums[0] + nums[1] <= nums[x]
        ))

        return (rs - 2) * (rs - 1) * rs // 6 + sum(
            l - bisect_left(nums, True, hi=l, key=lambda x: (
                nums[l] + x > nums[r]
            ))
            for r in range(rs, n)
            if nums[r - 2] + nums[r - 1] > nums[r]
            for l in range(
                1 + bisect_left(range(1, r), True, key=lambda x: (
                    nums[x - 1] + nums[x] > nums[r]
                )),
                r
            )
        )
        
# CODE-END
