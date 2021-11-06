# -*- coding: utf-8 -*-
from typing import Optional


class TreeNode:
    ''' Definition for a binary tree node. '''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ''' DFS solution. '''
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return
            if node.left:
                if not node.left.left and not node.left.right:
                    nonlocal ans
                    ans += node.left.val
                else:
                    dfs(node.left)
            dfs(node.right)

        ans = 0
        dfs(root)
        return ans


def main():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert Solution().sumOfLeftLeaves(root) == 24

    root = TreeNode(1)
    assert Solution().sumOfLeftLeaves(root) == 0


if __name__ == '__main__':
    main()
