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
        # how about storing profits into buy prices and let it accumulate into one number
        bp = [prices[0]] * 2
        p = [0] * 2
        for price in prices:
            bp[0] = min(bp[0], price)
            p[0] = max(p[0], price - bp[0])
            bp[1] = min(bp[1], price - p[0])
            p[1] = max(p[1], price - bp[1])

        return p[1]

        # T[i][k] = max profit on the end of ith day having had k transactions finished
        # T[i][k][0] = not having the stock
        # T[i][k][1] = having the stock
        #
        # T[-1][0][0] = 0, T[-1][0][1] = -inf
        # not have
        # T[i][k][0] = max(T[i-1][k-1][1] + price[i], T[i-1][k][0])
        # have
        # T[i][k][1] = max(T[i-1][k][0] - price[i], T[i-1][k][1])

        # bp1 = prices[0]
        # profit1 = 0
        # bp2 = prices[0]
        # profit2 = 0
        # for price in prices:
        #     bp1 = min(bp1, price)
        #     profit1 = max(profit1, price - bp1)
        #     bp2 = min(bp2, price - profit1)
        #     profit2 = max(profit2, price - bp2)
        # return profit2

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
