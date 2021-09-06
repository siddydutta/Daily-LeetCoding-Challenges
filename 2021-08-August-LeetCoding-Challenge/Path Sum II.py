# -*- coding: utf-8 -*-
from typing import List


class TreeNode:
    ''' Definition for a binary tree node. '''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ''' DFS solution using recursion. '''
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def dfs(root: TreeNode, path: List) -> None:
            # Base Case
            if not root:
                return
            # Leaf Node Condition
            if not root.left and not root.right:
                path.append(root.val)
                if sum(path) == targetSum:
                    paths.append(path.copy())
                path.pop()         # To backtrack
                return

            path.append(root.val)  # Add current node to path
            dfs(root.left, path)   # Traverse left sub tree
            dfs(root.right, path)  # Traverse right sub tree
            path.pop()             # To backtrack

        paths = list()
        dfs(root, list())
        return paths


def main():
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(1)
    targetSum = 22
    assert Solution().pathSum(root, targetSum) == [[5, 4, 11, 2], [5, 8, 4, 5]]


if __name__ == '__main__':
    main()
