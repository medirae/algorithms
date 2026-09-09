# Category: algorithms
# Level: Medium
# Percent: 49.744797%



# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.
# 
#  
# Example 1:
# 
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# 
# 
# Example 2:
# 
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= nums.length <= 200
# 	1 <= nums[i] <= 100
# 
 

# CODE-START
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return False

        if n == 2:
            return nums[0] == nums[1]

        s = sum(nums)
        if s & 1:
            return False
        s //= 2

        return self.bitwise(nums, s)
        return self.hashset(nums, s)
        return self.dp_itr(nums, s)

    @staticmethod
    def bitwise(nums, s):
        b, i, n = 1, 0, len(nums)
        while i < n and not (b >> s) & 1:
            b |= b << nums[i]
            i += 1

        return bool((b >> s) & 1)

    @staticmethod
    def dp_itr(nums, s):
        dp = [0] * (s + 1)
        dp[0] = 1
        for num in nums:
            for v in range(s, num - 1, -1):
                dp[v] |= dp[v - num]

        return bool(dp[s])
    
    @staticmethod
    def hashset(nums, s):
        i, n = 0, len(nums)
        hs = {0}
        while s not in hs and i < n:
            hs |= set(filter(s.__ge__, map(nums[i].__add__, hs)))
            i += 1

        return s in hs
        
# CODE-END
