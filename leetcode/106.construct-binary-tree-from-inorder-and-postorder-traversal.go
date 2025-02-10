/*
 * @lc app=leetcode id=106 lang=golang
 *
 * [106] Construct Binary Tree from Inorder and Postorder Traversal
 *
 * https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
 *
 * algorithms
 * Medium (65.39%)
 * Likes:    8259
 * Dislikes: 139
 * Total Accepted:    749.2K
 * Total Submissions: 1.1M
 * Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
 *
 * Given two integer arrays inorder and postorder where inorder is the inorder
 * traversal of a binary tree and postorder is the postorder traversal of the
 * same tree, construct and return the binary tree.
 *
 *
 * Example 1:
 *
 *
 * Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
 * Output: [3,9,20,null,null,15,7]
 *
 *
 * Example 2:
 *
 *
 * Input: inorder = [-1], postorder = [-1]
 * Output: [-1]
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= inorder.length <= 3000
 * postorder.length == inorder.length
 * -3000 <= inorder[i], postorder[i] <= 3000
 * inorder and postorder consist of unique values.
 * Each value of postorder also appears in inorder.
 * inorder is guaranteed to be the inorder traversal of the tree.
 * postorder is guaranteed to be the postorder traversal of the tree.
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
func buildTree(inorder []int, postorder []int) *TreeNode {
	n := len(postorder)
	for left, right := 0, n-1; left < right; left, right = left+1, right-1 {
		postorder[left], postorder[right] = postorder[right], postorder[left]
	}

	inValtoIdx := make(map[int]int)
	for ndx, val := range inorder {
		inValtoIdx[val] = ndx
	}

	var helper func(postStart, postEnd, inStart, inEnd int) *TreeNode
	helper = func(postStart, postEnd, inStart, inEnd int) *TreeNode {
		if postStart > postEnd || inStart > inEnd {
			return nil
		}
		val := postorder[postStart]
		node := &TreeNode{Val: val}
		ndx := inValtoIdx[val]
		rightSize := inEnd - ndx
		node.Right = helper(postStart+1, postStart+rightSize, ndx+1, inEnd)
		node.Left = helper(postStart+rightSize+1, postEnd, inStart, ndx-1)
		return node
	}
	return helper(0, n-1, 0, n-1)
}

// @lc code=end

