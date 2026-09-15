# Category: algorithms
# Level: Medium
# Percent: 74.30052%



# A conveyor belt has packages that must be shipped from one port to another within days days.
# 
# The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
# 
# Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.
# 
#  
# Example 1:
# 
# Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
# Output: 15
# Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
# 1st day: 1, 2, 3, 4, 5
# 2nd day: 6, 7
# 3rd day: 8
# 4th day: 9
# 5th day: 10
# 
# Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
# 
# 
# Example 2:
# 
# Input: weights = [3,2,2,4,1,4], days = 3
# Output: 6
# Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
# 1st day: 3, 2
# 2nd day: 2, 4
# 3rd day: 1, 4
# 
# 
# Example 3:
# 
# Input: weights = [1,2,3,1,1], days = 4
# Output: 3
# Explanation:
# 1st day: 1
# 2nd day: 2
# 3rd day: 3
# 4th day: 1, 1
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= days <= weights.length <= 5 * 10⁴
# 	1 <= weights[i] <= 500
# 
 

# CODE-START
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        wl = len(weights)
        wm = max(weights)
        mi, ma = max(wm, sum(weights) // days), ceil(wl / days) * wm 

        ps = [0]
        for w in weights:
            ps.append(ps[-1] + w)

        def pick(sc):
            ndx = d = 0
            while ndx < wl and d < days:
                ndx = bisect_right(ps, sc + ps[ndx], lo=ndx) - 1
                d += 1

            return ndx == wl

        return mi + bisect_left(range(mi, ma + 1), True, key=pick)
        
# CODE-END
