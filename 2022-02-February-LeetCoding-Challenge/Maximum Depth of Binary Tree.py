# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        ''' DFS solution. '''
        if not root:
            return 0

        def dfs(root: TreeNode, depth: int = 1) -> None:
            ''' If leaf node, appends depth, else adds one. '''
            if not root.left and not root.right:
                depths.append(depth)
                return
            if root.left:
                dfs(root.left, depth+1)
            if root.right:
                dfs(root.right, depth+1)

        depths = list()
        dfs(root)
        return max(depths)


def main():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert Solution().maxDepth(root) == 3

    root = TreeNode(1)
    root.right = TreeNode(2)
    assert Solution().maxDepth(root) == 2


if __name__ == '__main__':
    main()
