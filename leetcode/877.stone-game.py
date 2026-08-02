# Category: algorithms
# Level: Medium
# Percent: 73.49514%



# Alice and Bob play a game with piles of stones. There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].
# 
# The objective of the game is to end with the most stones. The total number of stones across all the piles is odd, so there are no ties.
# 
# Alice and Bob take turns, with Alice starting first. Each turn, a player takes the entire pile of stones either from the beginning or from the end of the row. This continues until there are no more piles left, at which point the person with the most stones wins.
# 
# Assuming Alice and Bob play optimally, return true if Alice wins the game, or false if Bob wins.
# 
#  
# Example 1:
# 
# Input: piles = [5,3,4,5]
# Output: true
# Explanation: 
# Alice starts first, and can only take the first 5 or the last 5.
# Say she takes the first 5, so that the row becomes [3, 4, 5].
# If Bob takes 3, then the board is [4, 5], and Alice takes 5 to win with 10 points.
# If Bob takes the last 5, then the board is [3, 4], and Alice takes 4 to win with 9 points.
# This demonstrated that taking the first 5 was a winning move for Alice, so we return true.
# 
# 
# Example 2:
# 
# Input: piles = [3,7,2,3]
# Output: true
# 
# 
#  
# Constraints:
# 
# 
# 	2 <= piles.length <= 500
# 	piles.length is even.
# 	1 <= piles[i] <= 500
# 	sum(piles[i]) is odd.
# 
 

# CODE-START
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        """
        Let the piles be P(0), P(1), ..., P(2n-1) where len(piles) == 2n.
        Let E(n) = P(0) + P(2) + ... + P(2n - 2).
        Let O(n) = P(1) + P(3) + ... + P(2n - 1).
        Having sum(P(n)) = O(n) + E(n) is odd, therefore E != O, therefore either O > E, or E > O.

        At first, the two available piles are l=0 (even) and r=2n - 1 (odd).
        Presuming Alice wants to take all even-indexed piles:
            Suppose the interval is P(l), P(l + 1), ... P(r).
            Since r - l + 1 is always even (because every full round removed two piles),
                r - l is odd.
            Thus l and r have opposite parity for every full round (alice takes one and bob takes one).
            Therefore one end is even and the other is odd.
            Alice's strategy: If there's an even pile, she takes it, which there always is.
                Bob get's the remaining end, which is always odd.
                After k rounds, Alice has taken k + 1 even-indexed piles, and Bob k odd-indexed piles.
                    That goes on to 2n - 1. So Alice can take all even-indexed piles.
        If Alice chose to do the same thing with odd-indexed piles, she could take them.
        So depending on whether O > E or E > O, alice chooses which indexes to take and will always win.
        
        Alice's score = max(E, O) > min(E, O) = Bob's score.
        """
        return True

        # if odd and even constraints are not there
        n = len(piles)
        dp = piles[:]
        for depth in range(n - 1, 0, -1):
            tdp = list()
            for left in range(depth):
                right = left + n - depth
                tdp.append(max(
                    piles[right] - dp[left],
                    piles[left] - dp[left + 1],
                ))

            dp = tdp
        
        return dp[0] > 0
        
# CODE-END
