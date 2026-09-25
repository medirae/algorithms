# Category: algorithms
# Level: Medium
# Percent: 38.883797%



# You are given three positive integers: n, index, and maxSum. You want to construct an array nums (0-indexed) that satisfies the following conditions:
# 
# 
# 	nums.length == n
# 	nums[i] is a positive integer where 0 <= i < n.
# 	abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
# 	The sum of all the elements of nums does not exceed maxSum.
# 	nums[index] is maximized.
# 
# 
# Return nums[index] of the constructed array.
# 
# Note that abs(x) equals x if x >= 0, and -x otherwise.
# 
#  
# Example 1:
# 
# Input: n = 4, index = 2,  maxSum = 6
# Output: 2
# Explanation: nums = [1,2,2,1] is one array that satisfies all the conditions.
# There are no arrays that satisfy all the conditions and have nums[2] == 3, so 2 is the maximum nums[2].
# 
# 
# Example 2:
# 
# Input: n = 6, index = 1,  maxSum = 10
# Output: 3
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= n <= maxSum <= 10⁹
# 	0 <= index < n
# 
 

# CODE-START
class Solution:
    def maxValue(self, n: int, x: int, masl: int) -> int:
        """
        a = array
        len(a) = n, 1 <= n <= masl <= 10 ** 9
        x = index
        a[x] = xv = max(a)

        r ∈ {-1, 0, 1}
        a[i] ∈ ℕ⁺
        P(i) = max(0, min(xv, a[i - 1] + r)), 0 < i <= n - 1
        N(i) = max(0, min(xv, a[i + 1] + r)), 0 <= i < n - 1
        a = [a[0], P(1), ..., P(x - 1), xv, N(x + 1), ..., N(n - 2), a[n - 1]]

        masl = sum(a) maximum limit
        mas = min(masl, max(sum(a)))
        mis = min(sum(a))

        max(xv) max sum:
            a[i] = xv
            sum = n * xv
                -> 0 <= sum <= masl
                -> 0 <= xv <= masl // n
                -> max(xv) = masl // n

        max(xv) min sum:
            a[0] = xv - x
            a[n - 1] = xv + x - n + 1
            sum = (xv - x) + (xv - x + 1) + ... + (xv - 1) + xv + (xv - 1) + ... + (xv + x - n) + (xv + x - n + 1)
                = n * xv - (1 + 2 + ... + x) - (1 + 2 + ... + (n - 1 - x))
                = n * xv - x * (x + 1) / 2 - (n - 1 - x) * (n - x) / 2
                = n * xv + n * x + n / 2 - n ** 2 / 2 - x ** 2 - x

                -> 0 <= sum <= masl
                -> 0 <= xv <= (masl - n * x - n / 2 + n ** 2 / 2 + x ** 2 + x) // n
                -> max(xv) = (masl - n * x - n / 2 + n ** 2 / 2 + x ** 2 + x) // n
        
        xv range:
            masl // n <= xv <= (masl - n * x - n / 2 + n ** 2 / 2 + x ** 2 + x) // n

        xv at optimum sum:
            xv = 1 -> [1, 1, ... 1, ..., 1, 1]
            xv = 2 -> [1, 1, ... 1, 2, 1, ... ,1, 1]
            xv = 3 -> [1, 1, ... 1, 2, 3, 2, 1, ..., 1, 1]
            left side:
                total count: xn = x
                number of values: ∀ v ∈ {1, ..., xv - 1}: xnv = min(xn, xv - 1) = min(x, xv - 1)
                cutoff value at index limit: xc = max(0, xv - 1 - xn) = max(0, xv - 1 - x)
                sum of extra summed values at cutoff: xes = xc * (xc + 1) / 2
                sum = ((xv - 1) + ... + 2 + 1) + (1 + ... + 1)
                    = (xv - 1) * xv / 2 + (xn - xnv) - xes

            right side:
                total count: xn = n - x - 1
                number of values: ∀ v ∈ {1, ..., xv - 1}: xnv = min(xn, xv - 1) = min(n - x - 1, xv - 1)
                cutoff value at index limit: xc = max(0, xv - 1 - xn) = max(0, xv - n + x)
                sum of extra summed values at cutoff: xes = xc * (xc + 1) / 2
                sum = xv - 1 + ... + 2 + 1 + ... + 1
                    = (xv - 1) * xv / 2 + (xn - xnv) - xes

            sum = xv + 
                (xv - 1) * xv / 2 + (lxn - lxnv) - lxes +
                (xv - 1) * xv / 2 + (rxn - rxnv) - rxes
                = xv^2
                x - lxnv - lxes +
                n - x - 1 - rxnv - rxes
                = xv^2 + n - 1 - (lxnv + rxnv) - (lxes + rxes)
        """

        def sv(xv):
            lxnv, rxnv = min(x, xv - 1), min(n - x - 1, xv - 1)
            lxc, rxc = max(0, xv - 1 - x), max(0, xv - n + x)
            lxes, rxes = lxc * (lxc + 1) // 2, rxc * (rxc + 1) // 2
            return xv ** 2 + n - 1 - (lxnv + rxnv) - (lxes + rxes)

        mi = int(masl // n)
        ma = int((masl - n * x - n // 2 + n ** 2 // 2 + x ** 2 + x) // n)
        if mi == ma:
            return mi

        return mi - 1 + bisect_right(range(mi, ma + 1), masl, key=sv)
        
# CODE-END
