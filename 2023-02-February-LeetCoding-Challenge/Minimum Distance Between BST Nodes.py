# -*- coding: utf-8 -*-
from math import inf
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            inorder(node.left)
            nonlocal prev
            if prev is not None:
                nonlocal res
                res = min(res, node.val - prev)
            prev = node.val
            inorder(node.right)

        prev, res = None, inf
        inorder(root)
        return res


def main():
    # test cases from leetcode
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    assert Solution().minDiffInBST(root) == 1

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(48)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(49)
    assert Solution().minDiffInBST(root) == 1


if __name__ == '__main__':
    main()
