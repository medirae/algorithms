# Category: algorithms
# Level: Medium
# Percent: 65.51323%



# A string s is called happy if it satisfies the following conditions:
# 
# 
# 	s only contains the letters 'a', 'b', and 'c'.
# 	s does not contain any of "aaa", "bbb", or "ccc" as a substring.
# 	s contains at most a occurrences of the letter 'a'.
# 	s contains at most b occurrences of the letter 'b'.
# 	s contains at most c occurrences of the letter 'c'.
# 
# 
# Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".
# 
# A substring is a contiguous sequence of characters within a string.
# 
#  
# Example 1:
# 
# Input: a = 1, b = 1, c = 7
# Output: "ccaccbcc"
# Explanation: "ccbccacc" would also be a correct answer.
# 
# 
# Example 2:
# 
# Input: a = 7, b = 1, c = 0
# Output: "aabaa"
# Explanation: It is the only correct answer in this case.
# 
# 
#  
# Constraints:
# 
# 
# 	0 <= a, b, c <= 100
# 	a + b + c > 0
# 
 

# CODE-START
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        h = list()
        if a:
            h.append((-a, 'a'))
        if b:
            h.append((-b, 'b'))
        if c:
            h.append((-c, 'c'))

        o = list()
        heapq.heapify(h)
        while h:
            if o[-2:] == [h[0][1]] * 2:
                fc, fch = heapq.heappop(h)
                if not h:
                    break

                sc, sch = heapq.heappop(h)
                o.append(sch)
                if -sc - 1 > 0:
                    heapq.heappush(h, (sc + 1, sch))
                
                heapq.heappush(h, (fc, fch))
            else:
                fc, fch = heapq.heappop(h)
                o.append(fch)
                if -fc - 1 > 0:
                    heapq.heappush(h, (fc + 1, fch))

        return ''.join(o)
# CODE-END
