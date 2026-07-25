# Category: algorithms
# Level: Medium
# Percent: 66.452705%



# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# 
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
# 
#  
# Example 1:
# 
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# 
# 
# Example 2:
# 
# Input: digits = "2"
# Output: ["a","b","c"]
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= digits.length <= 4
# 	digits[i] is a digit in the range ['2', '9'].
# 
 

# CODE-START
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        lmap = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz',
        }

        current = list()
        combs = list()
        def dfs(dndx: int):
            digit = digits[dndx]
            for letter in lmap[digit]:
                current.append(letter)
                if len(current) == n:
                    combs.append("".join(current))
                elif dndx < n - 1:
                    dfs(dndx + 1)
                current.pop()

        for dndx in range(n):
            dfs(dndx)

        return combs
        
# CODE-END
