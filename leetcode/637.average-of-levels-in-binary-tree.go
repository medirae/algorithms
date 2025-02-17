/*
 * @lc app=leetcode id=637 lang=golang
 *
 * [637] Average of Levels in Binary Tree
 *
 * https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
 *
 * algorithms
 * Easy (73.70%)
 * Likes:    5388
 * Dislikes: 342
 * Total Accepted:    610.5K
 * Total Submissions: 828K
 * Testcase Example:  '[3,9,20,null,null,15,7]'
 *
 * Given the root of a binary tree, return the average value of the nodes on
 * each level in the form of an array. Answers within 10^-5 of the actual
 * answer will be accepted.
 *
 * Example 1:
 *
 *
 * Input: root = [3,9,20,null,null,15,7]
 * Output: [3.00000,14.50000,11.00000]
 * Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5,
 * and on level 2 is 11.
 * Hence return [3, 14.5, 11].
 *
 *
 * Example 2:
 *
 *
 * Input: root = [3,9,20,15,7]
 * Output: [3.00000,14.50000,11.00000]
 *
 *
 *
 * Constraints:
 *
 *
 * The number of nodes in the tree is in the range [1, 10^4].
 * -2^31 <= Node.val <= 2^31 - 1
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
func averageOfLevels(root *TreeNode) []float64 {
	var result []float64
	que := []*TreeNode{root}
	for len(que) > 0 {
		var tmp []*TreeNode
		var count, sum float64
		for _, node := range que {
			if node == nil {
				continue
			}
			tmp = append(tmp, node.Left)
			tmp = append(tmp, node.Right)
			sum += float64(node.Val)
			count++
		}
		if count > 0 {
			result = append(result, sum/count)
		}
		que = tmp
	}
	return result
}

// @lc code=end

