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
        nums.sort()
        n = len(nums)

        z = max(2, bisect_left(nums, 1))
        s = z + bisect_left(range(z, n), True, key=lambda x: (
            nums[0] + nums[1] <= nums[x]
        ))
        c = comb(s + 2 - z, 3)

        for i in range(s, n):
            if nums[i - 2] + nums[i - 1] > nums[i]:
                iv = nums[i]
                l, r = 0, i - 1
                while l < r:
                    if nums[l] + nums[r] > iv:
                        c += r - l
                        r -= 1
                    else:
                        l += 1

        return c
# CODE-END
