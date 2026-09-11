# Category: algorithms
# Level: Medium
# Percent: 52.546818%



# You are given an integer array nums and an integer target.
# 
# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.
# 
# 
# 	For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# 
# 
# Return the number of different expressions that you can build, which evaluates to target.
# 
#  
# Example 1:
# 
# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
# 
# 
# Example 2:
# 
# Input: nums = [1], target = 1
# Output: 1
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= nums.length <= 20
# 	0 <= nums[i] <= 1000
# 	0 <= sum(nums[i]) <= 1000
# 	-1000 <= target <= 1000
# 
 

# CODE-START
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if (s := sum(nums)) < abs(target) or (s + target) & 1:
            return 0

        return self.dp(nums, target)
        return self.bf(nums, target)

    @staticmethod
    def dp(nums, target):
        n = len(nums)
        dp = [dict() for _ in range(n + 1)]
        dp[n][target] = 1

        for ndx in range(n - 1, -1, -1):
            for s, c in dp[ndx + 1].items():
                if (v := s - nums[ndx]) not in dp[ndx]:
                    dp[ndx][v] = c
                else:
                    dp[ndx][v] += c
                
                if (v := s + nums[ndx]) not in dp[ndx]:
                    dp[ndx][v] = c
                else:
                    dp[ndx][v] += c

        return dp[0].get(0, 0)

    @staticmethod
    def bf(nums, target):
        n = len(nums)
        s = sum(nums)

        def bt(ndx=0, summ=0):
            if ndx == n:
                return int(summ == target)

            return bt(ndx + 1, summ - nums[ndx]) + bt(ndx + 1, summ + nums[ndx])

        return bt()
        
# CODE-END
