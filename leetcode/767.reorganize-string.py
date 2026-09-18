# Category: algorithms
# Level: Medium
# Percent: 57.341927%



# Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
# 
# Return any possible rearrangement of s or return "" if not possible.
# 
#  
# Example 1:
# Input: s = "aab"
# Output: "aba"
# Example 2:
# Input: s = "aaab"
# Output: ""
# 
#  
# Constraints:
# 
# 
# 	1 <= s.length <= 500
# 	s consists of lowercase English letters.
# 
 

# CODE-START
class Solution:
    def reorganizeString(self, s: str) -> str:
        h = [(-c, ch) for ch, c in Counter(s).items()]
        heapq.heapify(h)
        
        c, ch = heapq.heappop(h)
        o = [ch]
        if -c - 1 >= 1:
            heapq.heappush(h, (c + 1, ch))
        
        while h:
            c, ch = heapq.heappop(h)
            if ch == o[-1]:
                if not h:
                    return ""

                c, ch = heapq.heapreplace(h, (c, ch))

            o.append(ch)
            if -c - 1 >= 1:
                heapq.heappush(h, (c + 1, ch))
        
        return ''.join(o)
# CODE-END
