# Category: algorithms
# Level: Hard
# Percent: 54.798996%



# We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].
# 
# You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.
# 
# If you choose a job that ends at time X you will be able to start another job that starts at time X.
# 
#  
# Example 1:
# 
# 
# 
# Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
# Output: 120
# Explanation: The subset chosen is the first and fourth job. 
# Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
# 
# 
# Example 2:
# 
#  
# 
# Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
# Output: 150
# Explanation: The subset chosen is the first, fourth and fifth job. 
# Profit obtained 150 = 20 + 70 + 60.
# 
# 
# Example 3:
# 
# 
# 
# Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
# Output: 6
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= startTime.length == endTime.length == profit.length <= 5 * 10⁴
# 	1 <= startTime[i] < endTime[i] <= 10⁹
# 	1 <= profit[i] <= 10⁴
# 
 

# CODE-START
class Solution:
    def jobScheduling(self, sts: list[int], ets: list[int], ps: list[int]) -> int:
        return self.dynamicp(sts, ets, ps)
        return self.backtracking(sts, ets, ps)

    @staticmethod
    def dynamicp(sts, ets, ps):
        etdp, pdp = [0], [0]
        for st, et, p in sorted(zip(sts, ets, ps), key=itemgetter(1)):
            p += pdp[bisect_right(etdp, st) - 1]
            if p > pdp[-1]:
                pdp.append(p)
                etdp.append(et)

        return pdp[-1]

    @staticmethod
    def backtracking(sts, ets, ps):
        n = len(sts)
        ind = sorted(range(n), key=sts.__getitem__)

        memo = [-1] * n
        def bt(ndx):
            if memo[ndx] > -1:
                return memo[ndx]

            j = ind[ndx]
            ma = 0
            for i in range(
                bisect_left(
                    ind, ets[j],
                    lo=ndx + 1, key=sts.__getitem__
                ), n
            ):
                ma = max(ma, bt(i))

            memo[ndx] = ps[j] + ma
            return memo[ndx]

        return max(bt(i) for i in range(n))
# CODE-END
