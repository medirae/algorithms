# Category: algorithms
# Level: Medium
# Percent: 59.528214%



# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
# 
# Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.
# 
# You may assume that you have an infinite number of each kind of coin.
# 
# The final answer is guaranteed to fit into a signed 32-bit integer.
# 
#  
# Example 1:
# 
# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
# 
# 
# Example 2:
# 
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
# 
# 
# Example 3:
# 
# Input: amount = 10, coins = [10]
# Output: 1
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= coins.length <= 300
# 	1 <= coins[i] <= 5000
# 	All the values of coins are unique.
# 	0 <= amount <= 5000
# 
 

# CODE-START
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return self.dp_1d_itr(amount, coins)
        return self.dp_2d_itr(amount, coins)
        return self.dp_2d(amount, coins)
        return self.bt(amount, coins)

    @staticmethod
    def dp_1d_itr(amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for amount in range(coin, amount + 1):
                dp[amount] += dp[amount - coin]
        return dp[amount]

    @staticmethod
    def dp_2d_itr(amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = defaultdict(lambda: defaultdict(lambda: None))
        stack = deque([[amount, n - 1]])
        while stack:
            en, cndx = stack.pop()
            if dp[en][cndx] is not None:
                continue
            if en < 0 or cndx < 0:
                dp[en][cndx] = 0
                continue
            if en == 0:
                dp[en][cndx] = 1
                continue

            if dp[en][cndx - 1] is not None and \
               dp[en - coins[cndx]][cndx] is not None:
               dp[en][cndx] = dp[en][cndx - 1] + dp[en - coins[cndx]][cndx]
               continue

            stack.append((en, cndx))

            if dp[en][cndx - 1] is None:
                stack.append((en, cndx - 1))

            if dp[en - coins[cndx]][cndx] is None:
                stack.append((en - coins[cndx], cndx))

        return dp[en][cndx]

    @staticmethod
    def dp_2d(amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = dict()
        def bt(amount, cndx):
            if amount < 0:
                return 0
            if amount == 0:
                return 1
            if cndx == n:
                return 0
            if amount in dp and cndx in dp[amount]:
                return dp[amount][cndx]
            
            if amount not in dp:
                dp[amount] = dict()
            dp[amount][cndx] = bt(amount - coins[cndx], cndx) + bt(amount, cndx + 1)
            return dp[amount][cndx]

        return bt(amount, 0)

    @staticmethod
    def bt(amount: int, coins: List[int]) -> int:
        n = len(coins)
        picked = list()
        remaining = amount
        combs = 0
        def bt(cndx):
            nonlocal remaining, combs, picked
            if remaining == 0:
                combs += 1
                return
            if cndx == n:
                return
            
            for count in range(remaining // coins[cndx], -1, -1):
                remaining -= coins[cndx] * count
                picked.extend([coins[cndx]] * count)
                bt(cndx + 1)
                picked = picked[:-count]
                remaining += coins[cndx] * count
        
        bt(0)
        return combs
        
# CODE-END
