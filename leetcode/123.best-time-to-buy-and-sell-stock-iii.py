# Category: algorithms
# Level: Hard
# Percent: 54.231388%



# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# 
# Find the maximum profit you can achieve. You may complete at most two transactions.
# 
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
# 
#  
# Example 1:
# 
# Input: prices = [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
# 
# Example 2:
# 
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
# 
# 
# Example 3:
# 
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= prices.length <= 10⁵
# 	0 <= prices[i] <= 10⁵
# 
 

# CODE-START
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # T[i][k] = max profit on the end of ith day having had k transactions finished
        # T[i][k][0] = not having the stock
        # T[i][k][1] = having the stock
        #
        # T[-1][0][0] = 0, T[-1][0][1] = -inf
        #
        # not have
        # T[i][0][0] = 0
        # T[i][1][0] = max(T[i-1][0][1] + price[i], T[i-1][1][0])
        # T[i][2][0] = max(T[i-1][1][1] + price[i], T[i-1][2][0])
        # T[i][k][0] = max(T[i-1][k-1][1] + price[i], T[i-1][k][0])
        # have
        # T[i][0][1] = -price[i]
        # T[i][1][1] = max(T[i-1][1][0] - price[i], T[i-1][1][1])
        # T[i][2][1] = max(T[i-1][2][0] - price[i], T[i-1][2][1])
        # T[i][k][1] = max(T[i-1][k][0] - price[i], T[i-1][k][1])
        #
        # min-inclusive-days-behind = 2 * transactions-count     # for when you can have finished the last transaction today and not have a stock
        # min-exclusive-days-behind = 2 * transactions-count + 1 # for when you need an extra day to purchase the stock today and hold it

        ni = float('-inf')
        # have, nothave
        nh = [0, ni, ni]
        h = [ni, ni, ni]

        for price in prices:
            nh, h = [
                nh[0],
                max(nh[1], h[0] + price),
                max(nh[2], h[1] + price),
            ], [
                max(h[0], nh[0] - price),
                max(h[1], nh[1] - price),
                ni,
            ]

        return max(nh)
        
# CODE-END
