# -*- coding: utf-8 -*-
class TreeNode:
    ''' Definition for a binary tree node. '''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ''' Simple DFS using recursion. '''
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return False
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if not root.left and not root.right and root.val != 1:
            return False
        return root


class Solution1:
    ''' DFS through recursion using a helper method. '''
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def has_one(root: TreeNode) -> bool:
            if not root:
                return False
            left = has_one(root.left)  # Check left sub tree
            right = has_one(root.right)  # Check right sub tree
            if not left:
                # Left sub tree does not contain one
                root.left = None
            if not right:
                # Right sub tree does not contain one
                root.right = None
            # Return is root, left or right sub trees contain one
            return root.val == 1 or left or right
        if not has_one(root):
            root = None
        return root


def main():
    root = TreeNode(1)
    root.right = TreeNode(0)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(1)
    result = Solution().pruneTree(root)
    assert result
    assert result.right
    assert not result.right.left
    assert result.right


if __name__ == '__main__':
    main()
