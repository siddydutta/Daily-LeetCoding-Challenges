# -*- coding: utf-8 -*-
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def pre_order(node):
            if node is None:
                return
            if node.left is None and node.right is None:
                yield node.val
                return
            yield from pre_order(node.left)
            yield from pre_order(node.right)
        return list(pre_order(root1)) == list(pre_order(root2))


def main():
    root1 = TreeNode(3)
    root1.left = TreeNode(5)
    root1.right = TreeNode(1)
    root1.left.left = TreeNode(6)
    root1.left.right = TreeNode(2)
    root1.right.left = TreeNode(9)
    root1.right.right = TreeNode(8)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(4)
    root2 = TreeNode(3)
    root2.left = TreeNode(5)
    root2.right = TreeNode(1)
    root2.left.left = TreeNode(6)
    root2.left.right = TreeNode(7)
    root2.right.left = TreeNode(4)
    root2.right.right = TreeNode(2)
    root2.right.right.left = TreeNode(9)
    root2.right.right.right = TreeNode(8)
    assert Solution().leafSimilar(root1, root2)

    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root2 = TreeNode(1)
    root2.left = TreeNode(3)
    root2.right = TreeNode(2)
    assert not Solution().leafSimilar(root1, root2)


if __name__ == '__main__':
    main()
