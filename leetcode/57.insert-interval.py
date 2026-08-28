# Category: algorithms
# Level: Medium
# Percent: 45.592426%



# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# 
# Two intervals are considered overlapping if they share at least one point.
# 
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# 
# Return intervals after the insertion.
# 
# Note that you don't need to modify intervals in-place. You can make a new array and return it.
# 
#  
# Example 1:
# 
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# 
# 
# Example 2:
# 
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
# 
# 
#  
# Constraints:
# 
# 
# 	0 <= intervals.length <= 10⁴
# 	intervals[i].length == 2
# 	0 <= starti <= endi <= 10⁵
# 	intervals is sorted by starti in ascending order.
# 	newInterval.length == 2
# 	0 <= start <= end <= 10⁵
# 
 

# CODE-START
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return [newInterval]

        l, r = 0, n - 1
        while l < r:
            m = l + (r - l + 1) // 2
            if intervals[m][0] < newInterval[0]:
                l = m
            else:
                r = m - 1
        
        o = intervals[:l]
        if not (intervals[l][1] < newInterval[0] or intervals[l][0] > newInterval[1]):
            o.append([
                min(intervals[l][0], newInterval[0]),
                max(intervals[l][1], newInterval[1])
            ])
        elif intervals[l][1] < newInterval[0]:
            o.append(intervals[l])
            o.append(newInterval)
        else:
            o.append(newInterval)
            o.append(intervals[l])

        ndx = l + 1
        while ndx < n and intervals[ndx][0] <= o[-1][1]:
            o[-1][1] = max(o[-1][1], intervals[ndx][1])
            ndx += 1
        o.extend(intervals[ndx:])
        return o
        
# CODE-END
