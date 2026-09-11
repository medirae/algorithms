# Category: algorithms
# Level: Medium
# Percent: 70.05302%



# You are given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# 
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# 
# You must solve this problem without using the library's sort function.
# 
#  
# Example 1:
# 
# 
# Input: nums = [2,0,2,1,1,0]
# 
# Output: [0,0,1,1,2,2]
# 
# Explanation:
# 
# The array has two 0s, two 1s, and two 2s. Sorting them in-place places all 0s first, then all 1s, then all 2s.
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,0,1]
# 
# Output: [0,1,2]
# 
# Explanation:
# 
# The array has one each of 0, 1, and 2, arranged in-place in the order 0, 1, 2.
# 
# 
#  
# Constraints:
# 
# 
# 	n == nums.length
# 	1 <= n <= 300
# 	nums[i] is either 0, 1, or 2.
# 
# 
#  
# Follow up: Could you come up with a one-pass algorithm using only constant extra space?
 

# CODE-START
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        return self.countingsort(nums)
        return self.twopointers(nums)

    @staticmethod
    def countingsort(nums):
        c = Counter(nums)
        nums[:] = chain(repeat(0, c[0]), repeat(1, c[1]), repeat(2, c[2]))

    @staticmethod
    def twopointers(nums):
        n = len(nums)
        l, m, r = 0, 0, n - 1
        while m <= r:
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                l, m = l + 1, m + 1
            elif nums[m] == 1:
                m += 1
            else:
                nums[m], nums[r] = nums[r], nums[m]
                r -= 1
        
# CODE-END
