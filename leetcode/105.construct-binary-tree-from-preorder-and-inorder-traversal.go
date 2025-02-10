/*
 * @lc app=leetcode id=105 lang=golang
 *
 * [105] Construct Binary Tree from Preorder and Inorder Traversal
 *
 * https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
 *
 * algorithms
 * Medium (65.89%)
 * Likes:    15570
 * Dislikes: 554
 * Total Accepted:    1.5M
 * Total Submissions: 2.2M
 * Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
 *
 * Given two integer arrays preorder and inorder where preorder is the preorder
 * traversal of a binary tree and inorder is the inorder traversal of the same
 * tree, construct and return the binary tree.
 *
 *
 * Example 1:
 *
 *
 * Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
 * Output: [3,9,20,null,null,15,7]
 *
 *
 * Example 2:
 *
 *
 * Input: preorder = [-1], inorder = [-1]
 * Output: [-1]
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= preorder.length <= 3000
 * inorder.length == preorder.length
 * -3000 <= preorder[i], inorder[i] <= 3000
 * preorder and inorder consist of unique values.
 * Each value of inorder also appears in preorder.
 * preorder is guaranteed to be the preorder traversal of the tree.
 * inorder is guaranteed to be the inorder traversal of the tree.
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
func buildTree(preorder []int, inorder []int) *TreeNode {
	n := len(preorder)

	inValToIdx := make(map[int]int)
	for ndx := 0; ndx < n; ndx++ {
		inValToIdx[inorder[ndx]] = ndx
	}

	var helper func(preStart, preEnd, inStart, inEnd int) *TreeNode
	helper = func(preStart, preEnd, inStart, inEnd int) *TreeNode {
		if preStart > preEnd || inStart > inEnd {
			return nil
		}
		val := preorder[preStart]
		node := &TreeNode{Val: val}
		ndx := inValToIdx[val]
		leftSize := ndx - inStart
		node.Left = helper(preStart+1, preStart+leftSize, inStart, ndx-1)
		node.Right = helper(preStart+leftSize+1, preEnd, ndx+1, inEnd)
		return node
	}
	return helper(0, n-1, 0, n-1)
}

// @lc code=end

