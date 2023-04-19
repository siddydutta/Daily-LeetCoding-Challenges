# -*- coding: utf-8 -*-
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, length: int, is_right: bool) -> int:
            if not node:
                return
            nonlocal max_length
            max_length = max(max_length, length)
            dfs(node.left, length + 1 if is_right else 1, False)
            dfs(node.right, 1 if is_right else length + 1, True)
        max_length = 0
        dfs(root, 0, False)
        dfs(root, 0, True)
        return max_length


def main():
    root = TreeNode(1)
    root.right = TreeNode(1)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(1)
    root.right.right.left = TreeNode(1)
    root.right.right.right = TreeNode(1)
    root.right.right.left.right = TreeNode(1)
    root.right.right.left.right.right = TreeNode(1)
    assert Solution().longestZigZag(root) == 3

    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    root.left.right = TreeNode(1)
    root.left.right.left = TreeNode(1)
    root.left.right.right = TreeNode(1)
    root.left.right.left.right = TreeNode(1)
    assert Solution().longestZigZag(root) == 4

    root = TreeNode(1)
    assert Solution().longestZigZag(root) == 0


if __name__ == '__main__':
    main()
