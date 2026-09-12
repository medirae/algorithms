# Category: algorithms
# Level: Medium
# Percent: 47.752453%



# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# 
# A subarray is a contiguous non-empty sequence of elements within an array.
# 
#  
# Example 1:
# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:
# Input: nums = [1,2,3], k = 3
# Output: 2
# 
#  
# Constraints:
# 
# 
# 	1 <= nums.length <= 2 * 10⁴
# 	-1000 <= nums[i] <= 1000
# 	-10⁷ <= k <= 10⁷
# 
 

# CODE-START
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n, s, r = len(nums), 0, 0
        c = {0: 1}
        for v in nums:
            s += v
            r += c.get(s - k, 0)
            if s not in c:
                c[s] = 0

            c[s] += 1

        return r
        
# CODE-END
