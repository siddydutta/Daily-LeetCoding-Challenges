# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        def traverse(root: TreeNode, depth=1) -> None:
            if not root.left and not root.right:
                nonlocal max_depth
                max_depth = max(max_depth, depth)
                return
            if root.left:
                traverse(root.left, depth+1)
            if root.right:
                traverse(root.right, depth+1)

        max_depth = 0
        traverse(root)
        return max_depth


def main():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert Solution().maxDepth(root) == 3

    root = TreeNode(1)
    root.right = TreeNode(2)
    assert Solution().maxDepth(root) == 2


if __name__ == '__main__':
    main()
