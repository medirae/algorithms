# Category: algorithms
# Level: Medium
# Percent: 82.141914%



# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
# 
#  
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:
# Input: nums = [1]
# Output: [[1]]
# 
#  
# Constraints:
# 
# 
# 	1 <= nums.length <= 6
# 	-10 <= nums[i] <= 10
# 	All the integers of nums are unique.
# 
 

# CODE-START
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.back_tracking(nums)
        return self.in_place(nums)

    @staticmethod
    def in_place(ns):
        n = len(ns)
        r = list()

        def bt(i):
            if i == n:
                r.append(ns.copy())
                return

            for j in range(i, n):
                ns[i], ns[j] = ns[j], ns[i]
                bt(i + 1)
                ns[i], ns[j] = ns[j], ns[i]

        bt(0)
        return r

    @staticmethod
    def back_tracking(nums):
        n = len(nums)
        r = list()
        p = list()
        mask = 0
        def bt():
            nonlocal mask
            if len(p) == n:
                r.append(p.copy())
                return
            
            for sndx in range(n):
                bit = 1 << sndx
                if mask & bit:
                    continue
                mask |= bit
                p.append(nums[sndx])
                bt()
                p.pop()
                mask ^= bit

        bt()
        return r
        
# CODE-END
