/*
 * @lc app=leetcode id=200 lang=golang
 *
 * [200] Number of Islands
 *
 * https://leetcode.com/problems/number-of-islands/description/
 *
 * algorithms
 * Medium (61.35%)
 * Likes:    23514
 * Dislikes: 551
 * Total Accepted:    3.2M
 * Total Submissions: 5.3M
 * Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
 *
 * Given an m x n 2D binary grid grid which represents a map of '1's (land) and
 * '0's (water), return the number of islands.
 *
 * An island is surrounded by water and is formed by connecting adjacent lands
 * horizontally or vertically. You may assume all four edges of the grid are
 * all surrounded by water.
 *
 *
 * Example 1:
 *
 *
 * Input: grid = [
 * ⁠ ["1","1","1","1","0"],
 * ⁠ ["1","1","0","1","0"],
 * ⁠ ["1","1","0","0","0"],
 * ⁠ ["0","0","0","0","0"]
 * ]
 * Output: 1
 *
 *
 * Example 2:
 *
 *
 * Input: grid = [
 * ⁠ ["1","1","0","0","0"],
 * ⁠ ["1","1","0","0","0"],
 * ⁠ ["0","0","1","0","0"],
 * ⁠ ["0","0","0","1","1"]
 * ]
 * Output: 3
 *
 *
 *
 * Constraints:
 *
 *
 * m == grid.length
 * n == grid[i].length
 * 1 <= m, n <= 300
 * grid[i][j] is '0' or '1'.
 *
 *
 */
package main

// @lc code=start
func numIslands(grid [][]byte) int {
	n, m := len(grid), len(grid[0])
	var islands int
	directions := [][]int{[]int{0, -1}, []int{-1, 0}, []int{1, 0}, []int{0, 1}}
	for r := 0; r < n; r++ {
		for c := 0; c < m; c++ {
			if grid[r][c] == '0' {
				continue
			}
			islands++
			stack := [][]int{[]int{r, c}}
			for len(stack) > 0 {
				node := stack[len(stack)-1]
				stack = stack[:len(stack)-1]
				grid[node[0]][node[1]] = '0'
				for _, dirs := range directions {
					rd, cd := node[0]+dirs[0], node[1]+dirs[1]
					if 0 <= rd && rd < n && 0 <= cd && cd < m && grid[rd][cd] == '1' {
						stack = append(stack, []int{rd, cd})
					}
				}
			}
		}
	}
	return islands
}

// @lc code=end
