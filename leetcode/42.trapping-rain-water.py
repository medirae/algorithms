# Category: algorithms
# Level: Hard
# Percent: 67.80518%



# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
# 
#  
# Example 1:
# 
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# 
# 
# Example 2:
# 
# Input: height = [4,2,0,3,2,5]
# Output: 9
# 
# 
#  
# Constraints:
# 
# 
# 	n == height.length
# 	1 <= n <= 2 * 10⁴
# 	0 <= height[i] <= 10⁵
# 
 

# CODE-START
class Solution:
    def trap(self, h: List[int]) -> int:
        return self.two_pointers(h)
        return self.mono(h)

    @staticmethod
    def two_pointers(h):
        n = len(h)
        l, r = 0, n - 1
        lm = rm = 0
        s = 0
        while l < r:
            if h[l] <= h[r]:
                lm = max(lm, h[l])
                s += lm - h[l]
                l += 1
            else:
                rm = max(rm, h[r])
                s += rm - h[r]
                r -= 1
        
        return s

    @staticmethod
    def monotonic_stack(self, h):
        n = len(h)
        rm = lm = 0
        r, l = [0] * n, [0] * n
        rst, lst = list(), list()
        for ndx in range(n):
            while lst and h[lst[-1]] < lm:
                l[lst.pop()] = lm
            lm = max(lm, h[ndx])
            lst.append(ndx)

            ndx = n - 1 - ndx

            while rst and h[rst[-1]] < rm:
                r[rst.pop()] = rm
            rm = max(rm, h[ndx])
            rst.append(ndx)
        
        s = 0
        for ndx, val in enumerate(h):
            s += max(min(l[ndx], r[ndx]), val) - val

        return s
        
# CODE-END
