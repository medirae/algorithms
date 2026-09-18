# Category: algorithms
# Level: Medium
# Percent: 63.789463%



# Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.
# 
#  
# Example 1:
# 
# Input: nums = [1,1,2]
# Output:
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
# 
# 
# Example 2:
# 
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= nums.length <= 8
# 	-10 <= nums[i] <= 10
# 
 

# CODE-START
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        k = len(nums)
        nums = Counter(nums)
        o = list()
        p = list()
        def bt(k=k):
            if k == 0:
                o.append(p.copy())
                return

            for val in nums:
                if nums[val]:
                    nums[val] -= 1
                    p.append(val)
                    bt(k - 1)
                    p.pop()
                    nums[val] += 1
        
        bt()
        return o
        
# CODE-END
