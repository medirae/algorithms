# Category: algorithms
# Level: Medium
# Percent: 39.476162%



# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# 
# Notice that the solution set must not contain duplicate triplets.
# 
#  
# Example 1:
# 
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# 
# 
# Example 2:
# 
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# 
# 
# Example 3:
# 
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
# 
# 
#  
# Constraints:
# 
# 
# 	3 <= nums.length <= 3000
# 	-10⁵ <= nums[i] <= 10⁵
# 
 

# CODE-START
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # TODO: solve with Counter
        return self.two_sum_II(nums)
        return self.two_sum(nums)
        return self.naive(nums)

    @staticmethod
    def two_sum_II(nums):
        n = len(nums)
        r = list()
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            j, k = i + 1, n - 1
            while j < k:
                x, y, z = nums[i], nums[j], nums[k]
                summ = x + y + z
                if summ == 0:
                    r.append([x, y, z])
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                elif summ > 0:
                    k -= 1
                else:
                    j += 1
        
        return r

    @staticmethod
    def two_sum(nums):
        n = len(nums)
        values = set()
        for i in range(n):
            storage = dict()
            for j in range(n):
                storage[-nums[i] - nums[j]] = j
            
            for k in range(n):
                if nums[k] in storage and k != (j := storage[nums[k]]) and k != i and i != j:
                    values.add(tuple(sorted((nums[j], nums[i], nums[k]))))

        return list(values)

    @staticmethod
    def naive(nums):  # TLE
        n = len(nums)
        storage = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i != j:
                    storage[-(nums[i] + nums[j])].append((i, j))

        indices = set()
        for i in range(n):
            for ndxset in storage[nums[i]]:
                if i not in ndxset:
                    indices.add(tuple(sorted(map(nums.__getitem__, (i, *ndxset)))))

        return list(indices)
        
# CODE-END
