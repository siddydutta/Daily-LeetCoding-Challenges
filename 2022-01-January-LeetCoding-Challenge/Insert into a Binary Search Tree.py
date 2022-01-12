# -*- coding: utf-8 -*-
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class RecursiveSolution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ''' Recursive solution using BST principles. '''
        if root is None:
            return TreeNode(val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root


class IterativeSolution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ''' Iterative solution using BST principles. '''
        if root is None:
            return TreeNode(val)
        node = root
        while True:
            if node.val < val:
                if node.right is None:
                    node.right = TreeNode(val)
                    break
                else:
                    node = node.right
            else:
                if node.left is None:
                    node.left = TreeNode(val)
                    break
                else:
                    node = node.left
        return root


def main():
    for obj in [RecursiveSolution(), IterativeSolution()]:
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        val = 5
        result = obj.insertIntoBST(root, val)
        assert result.val == 4
        assert result.left.val == 2
        assert result.right.val == 7
        assert result.left.left.val == 1
        assert result.left.right.val == 3
        assert result.right.left.val == 5


if __name__ == '__main__':
    main()
