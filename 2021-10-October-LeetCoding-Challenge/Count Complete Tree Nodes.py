# -*- coding: utf-8 -*-
from typing import Optional


class TreeNode:
    ''' Definition for a binary tree node. '''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    '''
    Straightforward recursive solution.
    Time Complexity: O(n)
    '''
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        n_left = self.countNodes(root.left)
        n_right = self.countNodes(root.right)
        return 1 + n_left + n_right


class Solution2:
    '''
    Optimized recursive solution.
    Time Complexity: O(logn * logn)
    '''
    def __get_depth(self, node: Optional[TreeNode]):
        if not node:
            return 0
        return 1 + self.__get_depth(node.left)  # Complete binary tree

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth = self.__get_depth(root.left)
        right_depth = self.__get_depth(root.right)
        if left_depth == right_depth:
            # Left sub tree is perfect binary tree
            # Right sub tree is complete binary tree
            return pow(2, left_depth) + self.countNodes(root.right)
        else:
            # Left sub tree is complete binary tree
            # Right sub tree is perfect binary tree
            return pow(2, right_depth) + self.countNodes(root.left)


def main():
    for obj in [Solution1(), Solution2()]:
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        assert obj.countNodes(root) == 6

        root = TreeNode(1)
        assert obj.countNodes(root) == 1

        root = None
        assert obj.countNodes(root) == 0


if __name__ == '__main__':
    main()
