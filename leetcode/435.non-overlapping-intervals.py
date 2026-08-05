# Category: algorithms
# Level: Medium
# Percent: 57.41577%



# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
# 
# Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.
# 
#  
# Example 1:
# 
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
# 
# 
# Example 2:
# 
# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
# 
# 
# Example 3:
# 
# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= intervals.length <= 10⁵
# 	intervals[i].length == 2
# 	-5 * 10⁴ <= starti < endi <= 5 * 10⁴
# 
 

# CODE-START
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """ai generated
        Intuition:
            The reason earliest finishing works is:
                A longer-lasting interval blocks more future choices.
                    Example:
                        A: |--------|
                        B: |--|
                    If we choose A we lose the chance to lose many intervals afterwards.
                    If we choose B we leave maximum room for future intervals.
                The greedy choice is not merely "good now"; it creates the largest possible remaining search space.

        ------------
        Greedy Proof
        ------------
        1: The earliest finishing interval is always part of some optimal solution.
            G: Interval with the earliest end time
            O: Optimal solution
            O[1]: The first interval chosen by the optimal solution
                Because G has the smallest ending time: end(G) <= end(O[1])
                Now construct a new solution O': Replace O[1] with G. Keep all other intervals in O.
                We need to prove O' is still valid:
                    Suppose O contains: O[1], O[2], ...
                    Since these intervals do not overlap: start(O[2]) >= end(O[1])
                    But: end(G) <= end(O[1])
                    Therefore: start(O[2]) >= end(G) meaning G does not overlap with O[2].
                    The same argument applies to every argument after O[1].
                    Therefore replacing O[1] with G keeps the solution valid.
                    The number of intervals is unchanged: |O'| = |O|.
                    Hence O' is also optimal.
                So, there exists an optimal solution containing the greedy choice.
            
        2: After choosing the greedy interval, the remaining problem is identical.
            After selecting G, the only intervals we can choose next are intervals satisfying: start(i) >= end(G).
            All other intervals overlap with G and cannot be in any valid solution containing G.
            So the remaining task is: Among the intervals starting after end(G), choose the maximum number of non-overlapping intervals.
            This is exactly the same problem but with fewer intervals.
        
        - If there are no intervals: greedy = optimal
        - Induction
            Assume greedy is optimal for all problems with fewer than n intervals.
            For n intervals:
                1. Greedy chooses G, the interval with earliest finishing time.
                2. From (1) some optimal solution also contains G.
                3. After choosing G, the remaining problem has fewer intervals.
                4. By the induction hypothesis, greedy is optimal on the remaining problem.
            Therefore: greedy solution = G + optimal solution of remainder
            Since an optimal solution can also start with G: greedy solution is globally optimal.
        """
        intervals.sort(key=lambda x: x[1])
        count = 0
        last_kept_end = -5*10**4-1
        for start, end in intervals:
            if start < last_kept_end:
                count += 1
            else:
                last_kept_end = end
        
        return count
        
# CODE-END
