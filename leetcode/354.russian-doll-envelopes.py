# Category: algorithms
# Level: Hard
# Percent: 38.02838%



# You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.
# 
# One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.
# 
# Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).
# 
# Note: You cannot rotate an envelope.
# 
#  
# Example 1:
# 
# Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
# 
# 
# Example 2:
# 
# Input: envelopes = [[1,1],[1,1],[1,1]]
# Output: 1
# 
# 
#  
# Constraints:
# 
# 
# 	1 <= envelopes.length <= 10⁵
# 	envelopes[i].length == 2
# 	1 <= wi, hi <= 10⁵
# 
 

# CODE-START
class Solution:
    def maxEnvelopes(self, es: list[list[int]]) -> int:
        return self.greedy(es)
        return self.backtracking(es)

    @staticmethod
    def greedy(es):
        es.sort(key=lambda x: (x[0], -x[1]))
        lis = list()
        for _, h in es:
            ndx = bisect_left(lis, h)
            if ndx == len(lis):
                lis.append(h)
            else:
                lis[ndx] = h

        return len(lis)

    @staticmethod
    def backtracking(es):  # TLE :(
        hs = dict()
        for w, h in es:
            if w not in hs:
                hs[w] = set()
            
            hs[w].add(h)
        
        ws = sorted(hs.keys())
        wn = len(ws)
        for w in hs:
            hs[w] = sorted(hs[w])

        dp = dict()
        def bt(ndx=0, w=0, h=0):
            if (w, h) in dp:
                return dp[(w, h)]

            awx = bisect_right(ws, w, lo=ndx)
            if awx >= wn or ws[awx] <= w:
                return 0

            wcnt = 0
            m = 0
            while awx < wn:
                aw = ws[awx]
                awhs = hs[aw]
                hsn = len(awhs)
                ahx = bisect_right(awhs, h)
                if ahx >= hsn or awhs[ahx] <= h:
                    awx += 1
                    continue

                hcnt = 0
                while ahx < hsn:
                    if (v := 1 + bt(awx + 1, aw, awhs[ahx])) >= m:
                        m = v
                    else:
                        break

                    ahx += 1
                
                awx += 1

            dp[(w, h)] = m
            return m

        return bt()
# CODE-END
