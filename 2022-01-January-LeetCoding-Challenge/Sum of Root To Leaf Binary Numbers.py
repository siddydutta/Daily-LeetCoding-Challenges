# -*- coding: utf-8 -*-
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ''' Recursive DFS solution. '''
        def dfs(node: TreeNode, binary: str) -> None:
            if node is None:
                return  # Base condition
            binary += str(node.val)
            if node.left is None and node.right is None:
                # Condition for leaf node
                nonlocal ans
                ans += int(binary, 2)  # Convert binary string to integer
                return
            dfs(node.left, binary), dfs(node.right, binary)

        ans = 0
        dfs(root, str())
        return ans


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(1)
    assert Solution().sumRootToLeaf(root) == 22

    root = TreeNode(0)
    assert Solution().sumRootToLeaf(root) == 0


if __name__ == '__main__':
    main()
