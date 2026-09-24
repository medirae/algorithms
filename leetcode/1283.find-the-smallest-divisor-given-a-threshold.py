# Category: algorithms
# Level: Medium
# Percent: 66.380325%



# Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by it, and sum the division's result. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.
# 
# Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).
# 
# The test cases are generated so that there will be an answer.
# 
#  
# Example 1:
# 
# Input: nums = [1,2,5,9], threshold = 6
# Output: 5
# Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1. 
# If the divisor is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2). 
# 
# 
# Example 2:
# 
# Input: nums = [44,22,33,11,1], threshold = 5
# Output: 44
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= nums.length <= 5 * 10⁴
# 	1 <= nums[i] <= 10⁶
# 	nums.length <= threshold <= 10⁶
# 
 

# CODE-START
class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        n = len(nums)
        s = sum(nums)
        l, r = ceil(s / threshold), ceil(s / max(1, threshold - n))
        while l < r:
            d = l + (r - l) // 2
            if sum(ceil(x / d) for x in nums) <= threshold:
                r = d
            else:
                l = d + 1

        return r
# CODE-END
