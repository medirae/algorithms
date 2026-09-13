# Category: algorithms
# Level: Easy
# Percent: 51.59804%



# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
# 
#  
# Example 1:
# 
# Input: nums = [1,2,3,1], k = 3
# Output: true
# 
# 
# Example 2:
# 
# Input: nums = [1,0,1,1], k = 1
# Output: true
# 
# 
# Example 3:
# 
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= nums.length <= 10⁵
# 	-10⁹ <= nums[i] <= 10⁹
# 	0 <= k <= 10⁵
# 
 

# CODE-START
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
    
        return self.hashset(nums, k)
        return self.bitwise(nums, k)
    
    @staticmethod
    def hashset(nums, k):
        k += 1
        n = len(nums)
        s = set(nums[:k])
        if len(s) != min(k, n):
            return True

        for r in range(k, n):
            s.discard(nums[r - k])
            x = nums[r]
            if x in s:
                return True
            s.add(x)

        return False

    @staticmethod
    def bitwise(nums, k):
        k += 1
        n = len(nums)
        ps = ns = 0
        for r in range(min(k, n)):
            x = nums[r]
            if x >= 0:
                v = 1 << x
                if ps & v:
                    return True
                ps |= v
            else:
                v = 1 << -x
                if ns & v:
                    return True
                ns |= v

        for r in range(k, n):
            x = nums[r - k]
            if x >= 0:
                ps ^= 1 << x
            else:
                ns ^= 1 << -x

            x = nums[r]
            if x >= 0:
                v = 1 << x
                if ps & v:
                    return True                
                ps |= v
            else:
                v = 1 << -x
                if ns & v:
                    return True
                ns |= v
        
        return False
        
# CODE-END
