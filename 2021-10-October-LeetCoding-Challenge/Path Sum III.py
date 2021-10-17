# -*- coding: utf-8 -*-
from collections import defaultdict


class TreeNode:
    ''' Definition for a binary tree node. '''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ''' DFS solution based on 1. Two Sum. '''
    def pathSum(self, root: TreeNode, target: int) -> int:
        count = 0
        cache = defaultdict(int)  # Sums: Count
        cache[0] = 1

        def dfs(node, current_sum):
            if not node:
                return
            current_sum += node.val
            nonlocal count
            count += cache[current_sum - target]  # Number of paths
            cache[current_sum] += 1  # Sum exists while going deeper
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
            cache[current_sum] -= 1  # Backtrack

        dfs(root, 0)
        return count


def main():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(-3)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(2)
    root.left.left.left = TreeNode(3)
    root.left.left.right = TreeNode(-2)
    root.left.right.right = TreeNode(1)
    root.right.right = TreeNode(11)
    targetSum = 8
    assert Solution().pathSum(root, targetSum) == 3


if __name__ == '__main__':
    main()
