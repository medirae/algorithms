# Category: algorithms
# Level: Hard
# Percent: 50.731266%



# You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.
# 
# Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.
# 
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
# 
#  
# Example 1:
# 
# Input: k = 2, prices = [2,4,1]
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
# 
# 
# Example 2:
# 
# Input: k = 2, prices = [3,2,6,5,0,3]
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= k <= 100
# 	1 <= prices.length <= 1000
# 	0 <= prices[i] <= 1000
# 
 

# CODE-START
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # how about storing profits into buy prices and let it accumulate into one number
        K = k
        bp = [prices[0]] * (K + 1)
        p = [0] * (K + 1)
        for price in prices:
            bp[1] = min(bp[1], price)
            p[1] = max(p[1], price - bp[1])
            for k in range(2, K + 1):
                bp[k] = min(bp[k], price - p[k-1])
                p[k] = max(p[k], price - bp[k])

        return p[K]

        # not have:
        # T[i][k][0] = max(T[i-1][k-1][1] + prices[i], T[i-1][k][0])
        # have:
        # T[i][k][1] = max(T[i-1][k][0] - prices[i], T[i-1][k][1])
        K = k
        ni = float('-inf')
        if K >= len(prices) // 2: # no transaction limit
            nh, h = 0, ni
            for price in prices:
                nh, h = max(
                    nh, h + price
                ), max(
                    h, nh - price
                )
            
            return nh

        nh = [ni] * (K + 1)
        nh[0] = 0
        h = [ni] * (K + 1)
        print(f'\t    have={h}')
        print(f'\tnot have={nh}')
        for price in prices:
            h[0] = max(h[0], nh[0] - price)
            for k in range(1, K + 1):
                nh[k] = max(nh[k], h[k - 1] + price if k > 0 else ni)
                h[k] = max(h[k], nh[k] - price) if k < K else ni
            print(f'\n{price=}')
            print(f'\t    have={h}')
            print(f'\tnot have={nh}')

        return max(nh)
        
# CODE-END
