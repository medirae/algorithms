# Category: algorithms
# Level: Medium
# Percent: 68.93422%



# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
# 
#  
# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:
# Input: temperatures = [30,60,90]
# Output: [1,1,0]
# 
#  
# Constraints:
# 
# 
# 	1 <= temperatures.length <= 10⁵
# 	30 <= temperatures[i] <= 100
# 
 

# CODE-START
class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        n = len(t)
        rst = list()
        o = [0] * n
        for i in range(n):
            while rst and t[rst[-1]] < t[i]:
                ndx = rst.pop()
                o[ndx] = i - ndx

            rst.append(i)
        
        return o
        
# CODE-END
