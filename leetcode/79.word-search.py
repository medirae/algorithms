# Category: algorithms
# Level: Medium
# Percent: 47.75442%



# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
# 
#  
# Example 1:
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# 
# 
# Example 2:
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# 
# 
# Example 3:
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
# 
# 
#  
# Constraints:
# 
# 
# 	m == board.length
# 	n = board[i].length
# 	1 <= m, n <= 6
# 	1 <= word.length <= 15
# 	board and word consists of only lowercase and uppercase English letters.
# 
# 
#  
# Follow up: Could you use search pruning to make your solution faster with a larger board?
 

# CODE-START
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        return self.dfs(board, word)
        return self.itr(board, word)

    @staticmethod
    def dfs(board, word):
        n, m = len(board), len(board[0])
        w = len(word)
        if n * m < w:
            return False

        if (c := Counter(c for r in board for c in r)) & (wc := Counter(word)) != wc:
            return False
        elif c[word[0]] > c[word[-1]]:
            word = word[::-1]

        def difs(i, j, k):
            if board[i][j] != word[k]:
                return False

            if k == w - 1:
                return True

            bak, board[i][j] = board[i][j], '#'
            o = False
            if ((
                    i > 0 and
                    board[i - 1][j] == word[k + 1] and
                    difs(i - 1, j, k + 1)
                ) or (
                    i + 1 < n and 
                    board[i + 1][j] == word[k + 1] and
                    difs(i + 1, j, k + 1)
                ) or (
                    j > 0 and
                    board[i][j - 1] == word[k + 1] and
                    difs(i, j - 1, k + 1)
                ) or (
                    j + 1 < m and
                    board[i][j + 1] == word[k + 1] and
                    difs(i, j + 1, k + 1)
                )
            ):
                o = True

            board[i][j] = bak
            return o

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and difs(i, j, 0):
                    return True

        return False

    @staticmethod
    def itr(board, word):
        n, m = len(board), len(board[0])
        w = len(word)
        if n * m < w:
            return False
        
        q = list()
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    q.append((0, i, j, 0))

        while q:
            v, i, j, k = q.pop()
            
            if board[i][j] != word[k]:
                continue
            if k == w - 1:
                return True
            v |= 1 << (m * i + j)

            for x, y in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                x, y = i + x, j + y
                if not (0 <= x < n) or not (0 <= y < m):
                    continue
                
                if board[x][y] != word[k + 1]:
                    continue
                
                bit = 1 << (x * m + y)
                if bit & v:
                    continue
                
                q.append((v | bit, x, y, k + 1))
        
        return False
        
# CODE-END
