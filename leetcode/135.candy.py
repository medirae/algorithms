# Category: algorithms
# Level: Hard
# Percent: 48.831833%



# There are n children standing in a line.
# 
# Each child is assigned a rating value given in the integer array ratings.
# 
# You are giving candies to these children subjected to the following requirements:
# 
# 
# 	Each child must have at least one candy.
# 	Children with a higher rating get more candies than their neighbors.
# 
# 
# Return the minimum number of candies you need to have to distribute the candies to the children.
# 
#  
# Example 1:
# 
# Input: ratings = [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
# 
# 
# Example 2:
# 
# Input: ratings = [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
# The third child gets 1 candy because it satisfies the above two conditions.
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= n == ratings.length <= 5 * 10⁴
# 	0 <= ratings[i] <= 5 * 10⁴
# 
 

# CODE-START
class Solution:
    def candy(self, ratings: list[int]) -> int:
        return self.itr(ratings)
        return self.dp(ratings)

    @staticmethod
    def itr(rs):
        n = len(rs)
        c = n
        i = 1
        while i < n:
            if rs[i] == rs[i - 1]:
                i += 1
                continue

            p = 0
            while i < n and rs[i] > rs[i - 1]:
                p, c, i = p + 1, c + p + 1, i + 1

            if i == n:
                break

            v = 0
            while i < n and rs[i] < rs[i - 1]:
                v, c, i = v + 1, c + v + 1, i + 1

            c -= min(p, v)

        return c

    @staticmethod
    def dp(ratings):
        n = len(ratings)
        dp = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                dp[i] = dp[i - 1] + 1

        s = dp[n - 1]
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                dp[i] = max(dp[i + 1] + 1, dp[i])
            s += dp[i]

        return s
# CODE-END
