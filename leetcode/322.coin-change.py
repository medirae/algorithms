# Category: algorithms
# Level: Medium
# Percent: 48.780144%



# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# 
# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# 
# You may assume that you have an infinite number of each kind of coin.
# 
#  
# Example 1:
# 
# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# 
# 
# Example 2:
# 
# Input: coins = [2], amount = 3
# Output: -1
# 
# 
# Example 3:
# 
# Input: coins = [1], amount = 0
# Output: 0
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= coins.length <= 12
# 	1 <= coins[i] <= 2³¹ - 1
# 	0 <= amount <= 10⁴
# 
 

# CODE-START
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
    
        coins = list(filter(lambda c: c <= amount, set(coins)))
        nc = len(coins)
        cd = reduce(gcd, coins) if nc > 1 else 1
        if (
            not coins or 
            (nc == 1 and amount % coins[0] != 0) or
            (nc > 1 and amount % cd != 0)
        ):
            return -1

        if nc == 1:
            return amount // coins[0]
        if cd > 1:
            amount, coins = amount // cd, list(map(lambda c: c // cd, coins))

        return self.bitwise(coins, amount)
        return self.dp_bu(coins, amount)
        return self.dp_td(coins, amount)
        return self.bf_backtracking(coins, amount)

    @staticmethod
    def bitwise(coins, amount):
        am, cc = 1 << amount, 0
        while am and not am & 1:
            am = reduce(int.__or__, map(am.__rshift__, coins))
            cc += 1

        return cc if am & 1 else -1

    @staticmethod
    def dp_bu(coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for am in range(1, amount + 1):
            m = float('inf')
            for c in coins:
                if c > am:
                    break
                m = min(m, dp[am - c] + 1)

            dp[am] = m
        
        return dp[amount] if dp[amount] != float('inf') else -1

    @staticmethod
    def dp_td(coins, amount):
        coins = sorted(coins)
        dp = defaultdict(lambda: float('inf'))
        dp[0] = 0
        for c in coins:
            dp[c] = 1

        def bt(am=amount):
            if am in dp:
                return dp[am]

            m = float('inf')
            for c in coins:
                if c > am:
                    break

                if (v := bt(am - c)) != float('inf'):
                    m = min(m, v + 1)

            dp[am] = m
            return m

        v = bt()
        return v if v != float('inf') else -1

    @staticmethod
    def bf_backtracking(coins, amount):
        n = len(coins)
        def bt(i=0, remain=amount):
            if i == n:
                return remain == 0

            m = float('inf')
            for j in range(remain // coins[i] + 1):
                v = bt(i + 1, remain - j * coins[i])
                if v is False:
                    continue
                elif v is True:
                    v = 0

                m = min(m, v + j)

            return m
        
        v = bt()
        return v if v != float('inf') else -1
        
# CODE-END
