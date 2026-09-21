# Category: algorithms
# Level: Medium
# Percent: 49.31564%



# Given an integer array arr, return the length of a maximum size turbulent subarray of arr.
# 
# A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.
# 
# More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:
# 
# 
# 	For i <= k < j:
# 
# 	
# 		arr[k] > arr[k + 1] when k is odd, and
# 		arr[k] < arr[k + 1] when k is even.
# 	
# 	
# 	Or, for i <= k < j:
# 	
# 		arr[k] > arr[k + 1] when k is even, and
# 		arr[k] < arr[k + 1] when k is odd.
# 	
# 	
# 
# 
#  
# Example 1:
# 
# Input: arr = [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
# 
# 
# Example 2:
# 
# Input: arr = [4,8,12,16]
# Output: 2
# 
# 
# Example 3:
# 
# Input: arr = [100]
# Output: 1
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= arr.length <= 4 * 10⁴
# 	0 <= arr[i] <= 10⁹
# 
 

# CODE-START
class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:        
        n, m = len(arr), 1
        l, gt = 0, None

        for r in range(n - 1):
            if arr[r] < arr[r + 1]:
                if gt is False:
                    gt = not gt
                else:
                    m = max(m, r - l + 1)
                    gt = True
                    l = r
            elif arr[r] > arr[r + 1]:
                if gt is True:
                    gt = not gt
                else:
                    m = max(m, r - l + 1)
                    gt = False
                    l = r
            else:
                m = max(m, r - l + 1)
                l = r + 1
                gt = None

        m = max(m, n - l)
        return m
# CODE-END
