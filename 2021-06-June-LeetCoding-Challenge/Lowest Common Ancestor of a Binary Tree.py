# -*- coding: utf-8 -*-
class TreeNode:
    '''
    Definition for a binary tree node.
    '''
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    '''
    Bottom-up tree traversal.
    Time Complexity: O(n)
    '''
    def lowestCommonAncestor(self, root: 'TreeNode',
                             p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base Case
        if not root:
            return None

        # If root is either p, q; root becomes LCA
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)  # Traverse left
        right = self.lowestCommonAncestor(root.right, p, q)  # Traverse right

        # Both p, q are not null, the current node is LCA
        if left and right:
            return root
        # Otherwise check left or right sub trees respectively
        if left:
            return left
        else:
            return right


def main():
    obj = Solution()
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    p = root.left   # 5
    q = root.right  # 1
    assert obj.lowestCommonAncestor(root, p, q) == root         # 3

    p = root.left               # 5
    q = root.left.right.right   # 4
    assert obj.lowestCommonAncestor(root, p, q) == root.left    # 5

    root = TreeNode(1)
    root.left = TreeNode(2)
    p = root        # 1
    q = root.left   # 2
    assert obj.lowestCommonAncestor(root, p, q) == root         # 1


if __name__ == '__main__':
    main()
