# Category: algorithms
# Level: Medium
# Percent: 69.079605%



# Given an integer array nums and an integer k, return the kth largest element in the array.
# 
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# 
# Can you solve it without sorting?
# 
#  
# Example 1:
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
# Example 2:
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
# 
#  
# Constraints:
# 
# 
# 	1 <= k <= nums.length <= 10⁵
# 	-10⁴ <= nums[i] <= 10⁴
# 
 

# CODE-START
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = [float('-inf')]
        maximum = float('-inf')
        for num in nums:
            if len(q) < k:
                heapq.heappush(q, num)
                continue
            if num >= maximum:
                heapq.heappush(q, num)
                heapq.heappop(q)
                maximum = num
            elif num > q[0]:
                heapq.heappush(q, num)
                heapq.heappop(q)
        
        return q[0]
        
# CODE-END
