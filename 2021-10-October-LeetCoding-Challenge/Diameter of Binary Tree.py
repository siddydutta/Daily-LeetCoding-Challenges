# -*- coding: utf-8 -*-
from typing import Optional


class TreeNode:
    ''' Definition for a binary tree node. '''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ''' DFS based solution. '''
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode):
            if not node:
                return 0
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            nonlocal max_diameter
            max_diameter = max(max_diameter, left_depth+right_depth)
            return 1 + max(left_depth, right_depth)

        max_diameter = 0
        dfs(root)
        return max_diameter


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    assert Solution().diameterOfBinaryTree(root) == 3

    root = TreeNode(1)
    root.left = TreeNode(2)
    assert Solution().diameterOfBinaryTree(root) == 1


if __name__ == '__main__':
    main()
