# -*- coding: utf-8 -*-
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                node.left, node.right = node.right, node.left
                queue.extend([node.left, node.right])
        return root


def main():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
    result = Solution().invertTree(root)
    assert result.val == 4
    assert result.left.val == 7
    assert result.right.val == 2
    assert result.left.left.val == 9
    assert result.left.right.val == 6
    assert result.right.left.val == 3
    assert result.right.right.val == 1

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    result = Solution().invertTree(root)
    assert result.val == 2
    assert result.left.val == 3
    assert result.right.val == 1

    root = None
    assert Solution().invertTree(root) is None


if __name__ == '__main__':
    main()
