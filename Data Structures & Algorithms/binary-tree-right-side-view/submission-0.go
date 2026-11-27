/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func rightSideView(root *TreeNode) []int {
    _, levelRightNodes := levelOrder(root)
	return levelRightNodes
}

func levelOrder(root *TreeNode) ([][]int, []int) {
	if root == nil {
		return nil, nil
	}

	result := [][]int{}
	resultRightNode := []int{}
	queue := []*TreeNode{root}

	for len(queue) > 0 {
		size := len(queue)
		level := []int{}
		levelRightNode := -1

		for i := 0; i < size; i++ {
			node := queue[0]
			queue = queue[1:]

			level = append(level, node.Val)
			levelRightNode = node.Val

			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}

		result = append(result, level)
		resultRightNode = append(resultRightNode, levelRightNode)
	}

	return result, resultRightNode
}
