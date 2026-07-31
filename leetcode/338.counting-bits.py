# Category: algorithms
# Level: Easy
# Percent: 80.755165%



# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
# Do not solve it with built-in functions (i.e., like __builtin_popcount in C++).
#  
# Example 1:
# 
# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 
# 
# Example 2:
# 
# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101
# 
# 
#  
# Constraints:
# 
# 
# 	0 <= n <= 10⁵
# 
# 
#  
# Follow up:
# 
# 
# 	It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
# 
 

# CODE-START
class Solution:
    def countBits(self, n: int) -> List[int]:
        arr = [0] * (n + 1)
        for i in range(1, n + 1):
            arr[i] = (i & 1) + arr[i >> 1]
        
        return arr

        if n == 0:
            return [0]
        arr = [0] * (n + 1)
        arr[1] = 1
        for p2 in range(1, ceil(log2(n + 1)) + 1):
            lower = 1 << (p2 - 1)
            for i in range(lower, min(2 * lower, n + 1)):
                arr[i] = arr[i - lower] + 1

        return arr
        
# CODE-END
