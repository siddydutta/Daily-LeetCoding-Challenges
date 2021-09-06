# -*- coding: utf-8 -*-
from typing import Optional


class TreeNode:
    ''' Definition for a binary tree node. '''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def get_sum(self, node: TreeNode) -> int:
        ''' Returns the sum of all nodes in the tree using DFS. '''
        if not node:
            return 0
        return node.val + self.get_sum(node.left) + self.get_sum(node.right)

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        tree_sum = self.get_sum(root)
        self.max_product = 0

        def dfs(node: TreeNode):
            if not node:
                return 0
            left_sum = dfs(node.left)    # Left sub tree sum
            right_sum = dfs(node.right)  # Right sub tree sum
            sub_tree_sum = node.val + left_sum + right_sum
            # Product is between current sub tree sum and rest of the tree sum
            self.max_product = max(self.max_product,
                                   sub_tree_sum * (tree_sum - sub_tree_sum))
            return sub_tree_sum

        dfs(root)
        return self.max_product % (10**9 + 7)


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    assert Solution().maxProduct(root) == 110

    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)
    root.right.right.left = TreeNode(5)
    root.right.right.right = TreeNode(6)
    assert Solution().maxProduct(root) == 90


if __name__ == '__main__':
    main()
