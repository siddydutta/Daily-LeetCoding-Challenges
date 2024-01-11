from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, high: int, low: int) -> int:
            if node is None:
                return high - low
            high, low = max(high, node.val), min(low, node.val)
            return max(dfs(node.left, high, low), dfs(node.right, high, low))
        return dfs(root, root.val, root.val)


def main():
    root = TreeNode(8)
    root.left = TreeNode(3)
    root.right = TreeNode(10)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.right.right = TreeNode(14)
    root.left.right.left = TreeNode(4)
    root.left.right.right = TreeNode(7)
    root.right.right.left = TreeNode(13)
    assert Solution().maxAncestorDiff(root) == 7

    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(0)
    root.right.right.left = TreeNode(3)
    assert Solution().maxAncestorDiff(root) == 3


if __name__ == '__main__':
    main()
