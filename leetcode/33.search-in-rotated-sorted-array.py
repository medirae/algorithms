# Category: algorithms
# Level: Medium
# Percent: 45.25873%



# There is an integer array nums sorted in ascending order (with distinct values).
# 
# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
# 
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
#  
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
# Input: nums = [1], target = 0
# Output: -1
# 
#  
# Constraints:
# 
# 
# 	1 <= nums.length <= 5000
# 	-10⁴ <= nums[i] <= 10⁴
# 	All values of nums are unique.
# 	nums is an ascending array that is possibly rotated.
# 	-10⁴ <= target <= 10⁴
# 
 

# CODE-START
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.onepass(nums, target)
        return self.findk(nums, target)

    @staticmethod
    def onepass(nums, target):
        n = len(nums)
        l, r = 0, n - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        
        return -1

    @staticmethod
    def findk(nums, target):
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1        

        l = n - 1
        if nums[0] > nums[-1]:
            l, r = 0, n - 1
            while l < r:
                m = l + (r - l + 1) // 2
                if nums[m] < nums[l]:
                    r = m - 1
                else:
                    l = m

        k = n - l - 1
        l, r = 0, n - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[(m - k) % n] == target:
                return (m - k) % n
            elif nums[(m - k) % n] < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1
        
# CODE-END
