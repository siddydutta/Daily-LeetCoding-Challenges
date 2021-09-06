# -*- coding: utf-8 -*-
from itertools import product
from typing import List, Optional


class TreeNode:
    ''' Definition for a binary tree node. '''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ''' Recursive solution with memoization. '''
    def __init__(self):
        self.cache = dict()

    def __generateSubTrees(self, low: int, high: int) -> List[TreeNode]:
        if (low, high) in self.cache:
            return self.cache.get((low, high))

        nodes = list()
        if low > high:
            nodes.append(None)
            return nodes
        for i in range(low, high+1):
            # Consider i to be root and construct left and right sub trees
            left_sub_trees = self.__generateSubTrees(low, i-1)
            right_sub_trees = self.__generateSubTrees(i+1, high)
            for left, right in product(left_sub_trees, right_sub_trees):
                # Create nodes for all combinations from left and right
                nodes.append(TreeNode(i, left, right))

        self.cache[(low, high)] = nodes
        return nodes

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.__generateSubTrees(1, n)


def main():
    # TODO: 98. Validate BST
    n = 3
    assert len(Solution().generateTrees(n)) == 5

    n = 1
    assert len(Solution().generateTrees(n)) == 1

    n = 8
    assert len(Solution().generateTrees(n)) == 1430


if __name__ == '__main__':
    main()
