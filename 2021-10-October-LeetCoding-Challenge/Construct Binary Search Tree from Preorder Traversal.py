# -*- coding: utf-8 -*-
from bisect import bisect
from typing import List, Optional


class TreeNode:
    ''' Definition for a binary tree node. '''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    '''
    Binary search and recursion based solution.
    Time Complexity: O(n^2)
    '''
    def bstFromPreorder(self, nodes: List[int]) -> Optional[TreeNode]:
        if not nodes:
            return None
        root = TreeNode(nodes[0])
        # Find index where nodes to the left are lesser and nodes to the right
        # are greater than the current root value
        index = bisect(nodes, nodes[0])
        root.left = self.bstFromPreorder(nodes[1:index])
        root.right = self.bstFromPreorder(nodes[index:])
        return root


def main():
    preorder = [8, 5, 1, 7, 10, 12]
    root = Solution().bstFromPreorder(preorder)
    assert root.val == 8
    assert root.left.val == 5
    assert root.left.left.val == 1
    assert root.left.right.val == 7
    assert root.right.val == 10
    assert not root.right.left
    assert root.right.right.val == 12

    preorder = [1, 3]
    root = Solution().bstFromPreorder(preorder)
    assert root.val == 1
    assert not root.left
    assert root.right.val == 3


if __name__ == '__main__':
    main()
