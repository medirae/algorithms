# Category: algorithms
# Level: Medium
# Percent: 41.155586%



# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 
# 
# 	0 <= a, b, c, d < n
# 	a, b, c, and d are distinct.
# 	nums[a] + nums[b] + nums[c] + nums[d] == target
# 
# 
# You may return the answer in any order.
# 
#  
# Example 1:
# 
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# 
# 
# Example 2:
# 
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= nums.length <= 200
# 	-10⁹ <= nums[i] <= 10⁹
# 	-10⁹ <= target <= 10⁹
# 
 

# CODE-START
class Solution:
    def fourSum(self, a: List[int], target: int) -> List[List[int]]:
        n = len(a)
        o = list()
        if n < 4:
            return o

        a.sort()
        i = 0
        while i < n - 3:
            if a[i] + a[i + 1] + a[i + 2] + a[i + 3] > target:
                break

            if a[i] < (mj := target - a[-3] - a[-2] - a[-1]):
                i = bisect_left(a, mj, i + 1, n - 3)
                continue

            if 0 < i and a[i] == a[i - 1]:
                i += 1
                continue

            j = i + 1
            while j < n - 2:
                if a[i] + a[j] + a[j + 1] + a[j + 2] > target:
                    break

                if a[i] < (mk := target - a[j] - a[-2] - a[-1]):
                    j = bisect_left(a, mk, j + 1, n - 2)
                    continue

                if i < j - 1 and a[j] == a[j - 1]:
                    j += 1
                    continue

                l, r = j + 1, n - 1
                t = target - a[i] - a[j]                
                while l < r:
                    s = a[l] + a[r]
                    if s < t:
                        l += 1
                    elif s > t:
                        r -= 1
                    else:
                        o.append([a[i], a[j], a[l], a[r]])

                        while l < r and a[l] == a[l + 1]:
                            l += 1

                        while l < r and a[r] == a[r - 1]:
                            r -= 1

                        l, r = l + 1, r - 1

                j += 1

            i += 1

        return o
        
# CODE-END
