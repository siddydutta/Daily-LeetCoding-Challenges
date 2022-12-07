# -*- coding: utf-8 -*-
from typing import Optional


# Definition of a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0
            range_sum = 0
            if low <= node.val <= high:
                range_sum += node.val
            if node.val > low:
                range_sum += dfs(node.left)
            if node.val < high:
                range_sum += dfs(node.right)
            return range_sum
        return dfs(root)


def main():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(18)
    low = 7
    high = 15
    assert Solution().rangeSumBST(root, low, high) == 32

    root.right.left = TreeNode(13)
    root.left.left.left = TreeNode(1)
    root.left.right.left = TreeNode(6)
    low = 6
    high = 10
    assert Solution().rangeSumBST(root, low, high) == 23


if __name__ == '__main__':
    main()
