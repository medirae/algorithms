/*
 * @lc app=leetcode id=102 lang=golang
 *
 * [102] Binary Tree Level Order Traversal
 *
 * https://leetcode.com/problems/binary-tree-level-order-traversal/description/
 *
 * algorithms
 * Medium (69.56%)
 * Likes:    15916
 * Dislikes: 339
 * Total Accepted:    2.7M
 * Total Submissions: 3.8M
 * Testcase Example:  '[3,9,20,null,null,15,7]'
 *
 * Given the root of a binary tree, return the level order traversal of its
 * nodes' values. (i.e., from left to right, level by level).
 *
 *
 * Example 1:
 *
 *
 * Input: root = [3,9,20,null,null,15,7]
 * Output: [[3],[9,20],[15,7]]
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
 * -1000 <= Node.val <= 1000
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
func levelOrder(root *TreeNode) (result [][]int) {
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
		if len(level) > 0 {
			result = append(result, level)
		}
		que = tmp
	}
	return result
}

// @lc code=end

