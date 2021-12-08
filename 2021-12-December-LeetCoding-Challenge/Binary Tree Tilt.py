# -*- coding: utf-8 -*-
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        ''' Recursive, straight-forward solution. '''
        def dfs(root):
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            nonlocal tilt
            tilt += abs(left - right)
            return root.val + left + right

        tilt = 0
        dfs(root)
        return tilt


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert Solution().findTilt(root) == 1

    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(9)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(7)
    assert Solution().findTilt(root) == 15

    root = TreeNode(21)
    root.left = TreeNode(7)
    root.right = TreeNode(14)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(2)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(3)
    assert Solution().findTilt(root) == 9


if __name__ == '__main__':
    main()
