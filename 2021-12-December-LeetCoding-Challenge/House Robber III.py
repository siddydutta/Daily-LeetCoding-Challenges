# -*- coding: utf-8 -*-
from functools import lru_cache
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        ''' Naive recursive solution. '''

        @lru_cache(None)
        def rob_node(node: TreeNode) -> int:
            ''' Return max money possible of sub-tree from node. '''
            if node is None:
                return 0

            val = node.val
            if node.left is not None:
                val += rob_node(node.left.left) + rob_node(node.left.right)
            if node.right is not None:
                val += rob_node(node.right.left) + rob_node(node.right.right)

            return max(val, rob_node(node.left) + rob_node(node.right))

        return rob_node(root)


def main():
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(1)
    assert Solution().rob(root) == 7

    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(1)
    assert Solution().rob(root) == 9


if __name__ == '__main__':
    main()
