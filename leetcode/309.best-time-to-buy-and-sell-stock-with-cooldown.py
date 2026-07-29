# Category: algorithms
# Level: Medium
# Percent: 62.433903%



# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# 
# Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
# 
# 
# 	After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
# 
# 
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
# 
#  
# Example 1:
# 
# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
# 
# 
# Example 2:
# 
# Input: prices = [1]
# Output: 0
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= prices.length <= 5000
# 	0 <= prices[i] <= 1000
# 
 

# CODE-START
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # T[i][sold] = T[i-1][have] + price[i]
        # T[i][watch] = max(T[i-1][sold], T[i-1][watch])
        # T[i][have] = max(T[i-1][have], T[i-1][watch] - price[i])

        ni = float('-inf')
        # sold, watch, have
        s, w, h = ni, 0, ni
        for price in prices:
            s, w, h = h + price, max(s, w), max(h, w - price)
        
        return max(s, w)
        
# CODE-END
