# Category: algorithms
# Level: Medium
# Percent: 49.9001%



# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
# 
# An integer a is closer to x than an integer b if:
# 
# 
# 	|a - x| < |b - x|, or
# 	|a - x| == |b - x| and a < b
# 
# 
#  
# Example 1:
# 
# 
# Input: arr = [1,2,3,4,5], k = 4, x = 3
# 
# Output: [1,2,3,4]
# 
# 
# Example 2:
# 
# 
# Input: arr = [1,1,2,3,4,5], k = 4, x = -1
# 
# Output: [1,1,2,3]
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= k <= arr.length
# 	1 <= arr.length <= 10⁴
# 	arr is sorted in ascending order.
# 	-10⁴ <= arr[i], x <= 10⁴
# 
 

# CODE-START
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        if n == k:
            return arr

        if x <= arr[0]:
            return arr[:k]

        if x >= arr[-1]:
            return arr[-k:]

        l, r = 0, n - 1
        xndx = None
        while l < r:
            m = l + (r - l + 1) // 2
            if arr[m] <= x:
                l = m
            else:
                r = m - 1

        if l < n and arr[l + 1] - x < x - arr[l]:
            xndx = l + 1
        else:
            xndx = l

        l = r = xndx
        for _ in range(k - 1):
            if 0 < l <= r < n - 1:
                if arr[r + 1] - x < x - arr[l - 1]:
                    r += 1
                else:
                    l -= 1
            elif r < n - 1:
                r += 1
            else:
                l -= 1

        return arr[l:r + 1]
        
# CODE-END
