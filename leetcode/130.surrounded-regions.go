/*
 * @lc app=leetcode id=130 lang=golang
 *
 * [130] Surrounded Regions
 *
 * https://leetcode.com/problems/surrounded-regions/description/
 *
 * algorithms
 * Medium (41.79%)
 * Likes:    9052
 * Dislikes: 2021
 * Total Accepted:    883.5K
 * Total Submissions: 2.1M
 * Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
 *
 * You are given an m x n matrix board containing letters 'X' and 'O', capture
 * regions that are surrounded:
 *
 *
 * Connect: A cell is connected to adjacent cells horizontally or
 * vertically.
 * Region: To form a region connect every 'O' cell.
 * Surround: The region is surrounded with 'X' cells if you can connect the
 * region with 'X' cells and none of the region cells are on the edge of the
 * board.
 *
 *
 * To capture a surrounded region, replace all 'O's with 'X's in-place within
 * the original board. You do not need to return anything.
 *
 *
 * Example 1:
 *
 *
 * Input: board =
 * [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
 *
 * Output:
 * [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
 *
 * Explanation:
 *
 * In the above diagram, the bottom region is not captured because it is on the
 * edge of the board and cannot be surrounded.
 *
 *
 * Example 2:
 *
 *
 * Input: board = [["X"]]
 *
 * Output: [["X"]]
 *
 *
 *
 * Constraints:
 *
 *
 * m == board.length
 * n == board[i].length
 * 1 <= m, n <= 200
 * board[i][j] is 'X' or 'O'.
 *
 *
 */

package main

// @lc code=start
func solve(board [][]byte) {
	dirs := [][]int{[]int{-1, 0}, []int{1, 0}, []int{0, -1}, []int{0, 1}}
	dfs := func(row, col, n, m int, board [][]byte) {
		if board[row][col] != 'O' {
			return
		}
		stack := [][]int{[]int{row, col}}
		for len(stack) > 0 {
			node := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			board[node[0]][node[1]] = 'R'
			for _, dir := range dirs {
				rd, cd := node[0]+dir[0], node[1]+dir[1]
				if 0 <= rd && rd < n && 0 <= cd && cd < m && board[rd][cd] == 'O' {
					stack = append(stack, []int{rd, cd})
				}
			}
		}
	}

	n, m := len(board), len(board[0])
	for row := 0; row < n; row++ {
		dfs(row, 0, n, m, board)
		dfs(row, m-1, n, m, board)
	}
	for col := 1; col < m-1; col++ {
		dfs(0, col, n, m, board)
		dfs(n-1, col, n, m, board)
	}
	for row := 0; row < n; row++ {
		for col := 0; col < m; col++ {
			switch board[row][col] {
			case 'R':
				board[row][col] = 'O'
			case 'O':
				board[row][col] = 'X'
			}
		}
	}
}

// @lc code=end
