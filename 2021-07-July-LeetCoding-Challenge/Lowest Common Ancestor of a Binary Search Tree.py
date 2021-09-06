# -*- coding: utf-8 -*-
class TreeNode:
    ''' Definition for a binary tree node. '''
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class NotSolution:
    ''' Recursive solution assuming a generic binary tree. '''
    def lowestCommonAncestor(self, root: 'TreeNode',
                             p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if left:
            return left
        else:
            return right


class Solution:
    ''' Reducing complexity of recursive solution using BST properties. '''
    def lowestCommonAncestor(self, root: 'TreeNode',
                             p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None  # Base case

        # If p, q are lesser than root -> traverse left subtree
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # If p, q are greater than root -> traverse right subtree
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # If both conditions are false, the root is the LCA
        else:
            return root


class NonRecursiveSolution:
    ''' Basic solution without using recursion. '''
    def lowestCommonAncestor(self, root: 'TreeNode',
                             p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            return root


def main():
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    p = root.left   # 2
    q = root.right  # 8
    assert Solution().lowestCommonAncestor(root, p, q) == root  # 6
    p = root.left       # 2
    q = root.left.left  # 4
    assert Solution().lowestCommonAncestor(root, p, q) == root.left  # 2

    root = TreeNode(2)
    root.left = TreeNode(1)
    p = root       # 2
    q = root.left  # 1
    assert Solution().lowestCommonAncestor(root, p, q) == root  # 2


if __name__ == '__main__':
    main()
