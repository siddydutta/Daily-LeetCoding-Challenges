# -*- coding: utf-8 -*-
from typing import Optional


class TreeNode:
    ''' Definition for a binary tree node. '''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ''' Recursive solution. '''
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return

        if root.val == key:
            if root.right is None:
                return root.left
            if root.left is None:
                return root.right

            if root.left and root.right:
                temp = root.right
                while temp.left:
                    temp = temp.left  # Find minimum
                root.val = temp.val
                root.right = self.deleteNode(root.right, root.val)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)

        return root


def main():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)
    key = 3
    result = Solution().deleteNode(root, key)
    assert result.val == 5
    assert result.left.val == 4
    assert result.right.val == 6
    assert result.left.left.val == 2
    assert result.left.right is None
    assert result.right.left is None
    assert result.right.right.val == 7

    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)
    key = 0
    result = Solution().deleteNode(root, key)
    assert result == root
    assert result.left == root.left
    assert result.right == root.right
    assert result.left.right == root.left.right
    assert result.right.right == root.right.right

    root = None
    key = 0
    assert Solution().deleteNode(root, key) is None


if __name__ == '__main__':
    main()
