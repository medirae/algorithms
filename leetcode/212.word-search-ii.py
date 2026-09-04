# Category: algorithms
# Level: Hard
# Percent: 38.669674%



# Given an m x n board of characters and a list of strings words, return all words on the board.
# 
# Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
# 
#  
# Example 1:
# 
# Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
# 
# 
# Example 2:
# 
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
# 
# 
#  
# Constraints:
# 
# 
# 	m == board.length
# 	n == board[i].length
# 	1 <= m, n <= 12
# 	board[i][j] is a lowercase English letter.
# 	1 <= words.length <= 3 * 10⁴
# 	1 <= words[i].length <= 10
# 	words[i] consists of lowercase English letters.
# 	All the strings of words are unique.
# 
 

# CODE-START
class Solution:
    def findWords(self, b: List[List[str]], words: List[str]) -> List[str]:
        class TN:
            __slots__ = ('p', 'd', 'w', 'c')
            def __init__(self, p=None, c=''):
                self.p = p
                self.d = dict()
                self.c = c
                self.w = False

            @classmethod
            def mkt(cls, words: list[str]) -> Self:
                t = cls()
                for word in words:
                    d = t
                    for c in word:
                        if c not in d.d:
                            d.d[c] = cls(p=d, c=c)

                        d = d.d[c]
                    
                    d.w = True
                return t

            def prune(self):
                self.w = False
                ad = self
                while len(ad.d) == 0:
                    c = ad.c
                    ad = ad.p
                    if ad is None:
                        break
                    del ad.d[c]

        n, m, w = len(b), len(b[0]), len(words)
        cn = Counter(chain(*b))
        for wndx in range(w - 1, -1, -1):
            if not (Counter(words[wndx]) <= cn):
                del words[wndx]

        w = len(words)
        t = TN.mkt(words)

        def dfs(i, j, s, d):
            o = list()
            if d.w:
                o.append(s)
                d.prune()

            if len(o) < w and i < n - 1 and (c := b[i + 1][j]) in d.d:
                b[i + 1][j] = None
                o.extend(dfs(i + 1, j, s + c, d.d[c]))
                b[i + 1][j] = c
            if len(o) < w and i > 0 and (c := b[i - 1][j]) in d.d:
                b[i - 1][j] = None
                o.extend(dfs(i - 1, j, s + c, d.d[c]))
                b[i - 1][j] = c
            if len(o) < w and j < m - 1 and (c := b[i][j + 1]) in d.d:
                b[i][j + 1] = None
                o.extend(dfs(i, j + 1, s + c, d.d[c]))
                b[i][j + 1] = c
            if len(o) < w and j > 0 and (c := b[i][j - 1]) in d.d:
                b[i][j - 1] = None
                o.extend(dfs(i, j - 1, s + c, d.d[c]))
                b[i][j - 1] = c

            return o

        o = list()
        for i in range(n):
            for j in range(m):
                if b[i][j] in t.d:
                    c = b[i][j]
                    b[i][j] = None
                    o.extend(dfs(i, j, c, t.d[c]))
                    b[i][j] = c
                    if len(o) >= w:
                        break

        return o
        
# CODE-END
