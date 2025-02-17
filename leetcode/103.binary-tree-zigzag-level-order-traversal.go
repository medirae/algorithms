/*
 * @lc app=leetcode id=103 lang=golang
 *
 * [103] Binary Tree Zigzag Level Order Traversal
 *
 * https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
 *
 * algorithms
 * Medium (60.80%)
 * Likes:    11228
 * Dislikes: 323
 * Total Accepted:    1.4M
 * Total Submissions: 2.3M
 * Testcase Example:  '[3,9,20,null,null,15,7]'
 *
 * Given the root of a binary tree, return the zigzag level order traversal of
 * its nodes' values. (i.e., from left to right, then right to left for the
 * next level and alternate between).
 *
 *
 * Example 1:
 *
 *
 * Input: root = [3,9,20,null,null,15,7]
 * Output: [[3],[20,9],[15,7]]
 *
 *
 * Example 2:
 *
 *
 * Input: root = [1]
 * Output: [[1]]
 *
 *
 * Example 3:
 *
 *
 * Input: root = []
 * Output: []
 *
 *
 *
 * Constraints:
 *
 *
 * The number of nodes in the tree is in the range [0, 2000].
 * -100 <= Node.val <= 100
 *
 *
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func zigzagLevelOrder(root *TreeNode) [][]int {
	var result [][]int
	var rtl bool
	que := []*TreeNode{root}
	for len(que) > 0 {
		var level []int
		var tmp []*TreeNode
		for _, node := range que {
			if node == nil {
				continue
			}
			tmp = append(tmp, node.Left)
			tmp = append(tmp, node.Right)
			level = append(level, node.Val)
		}
		if rtl {
			for i, j := 0, len(level)-1; i < j; i, j = i+1, j-1 {
				level[i], level[j] = level[j], level[i]
			}
		}
		rtl = !rtl
		if len(level) > 0 {
			result = append(result, level)
		}
		que = tmp
	}
	return result
}

// @lc code=end

