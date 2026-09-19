# Category: algorithms
# Level: Medium
# Percent: 38.76844%



# Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.
# 
#  
# Example 1:
# 
# Input: nums = [4,3,2,3,5,2,1], k = 4
# Output: true
# Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
# 
# 
# Example 2:
# 
# Input: nums = [1,2,3,4], k = 3
# Output: false
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= k <= nums.length <= 16
# 	1 <= nums[i] <= 10⁴
# 	The frequency of each element is in the range [1, 4].
# 
 

# CODE-START
class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        s = sum(nums)
        if s % k != 0:
            return False

        s //= k
        nums.sort(reverse=True)
        groups = [0] * k
        def bt(ndx=0):
            if ndx == n:
                return True

            v = set()
            for gndx in range(k):
                if groups[gndx] in v:
                    continue
                v.add(groups[gndx])
                if groups[gndx] + nums[ndx] > s:
                    continue

                groups[gndx] += nums[ndx]
                if bt(ndx + 1):
                    return True
                groups[gndx] -= nums[ndx]

            return False

        return bt()
# CODE-END
