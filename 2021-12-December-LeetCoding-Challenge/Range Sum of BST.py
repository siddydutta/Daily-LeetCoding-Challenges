# -*- coding: utf-8 -*-

# Definition of a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        ''' Recursive DFS solution. '''
        def dfs(root):
            if root is None:
                return
            # Range sum condition
            if root.val >= low and root.val <= high:
                # Range sum condition
                nonlocal range_sum
                range_sum += root.val
            # Property of binary search tree
            if root.val > low:
                dfs(root.left)
            if root.val < high:
                dfs(root.right)

        range_sum = 0
        dfs(root)
        return range_sum


def main():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(18)
    low = 7
    high = 15
    assert Solution().rangeSumBST(root, low, high) == 32

    root.right.left = TreeNode(13)
    root.left.left.left = TreeNode(1)
    root.left.right.left = TreeNode(6)
    low = 6
    high = 10
    assert Solution().rangeSumBST(root, low, high) == 23


if __name__ == '__main__':
    main()
