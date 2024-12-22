from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(
            node1: Optional[TreeNode], node2: Optional[TreeNode], level: int
        ) -> None:
            if not node1 or not node2:
                return
            if level % 2 != 0:
                node1.val, node2.val = node2.val, node1.val
            dfs(node1.left, node2.right, level+1)
            dfs(node1.right, node2.left, level+1)

        dfs(root.left, root.right, 1)
        return root


def main():
    root = TreeNode(2)
    root.left = TreeNode(3)
    root.right = TreeNode(5)
    root.left.left = TreeNode(8)
    root.left.right = TreeNode(13)
    root.right.left = TreeNode(21)
    root.right.right = TreeNode(34)
    result = Solution().reverseOddLevels(root)
    assert result.val == 2
    assert result.left.val == 5
    assert result.right.val == 3
    assert result.left.left.val == 8
    assert result.left.right.val == 13
    assert result.right.left.val == 21
    assert result.right.right.val == 34

    root = TreeNode(7)
    root.left = TreeNode(13)
    root.right = TreeNode(11)
    result = Solution().reverseOddLevels(root)
    assert result.val == 7
    assert result.left.val == 11
    assert result.right.val == 13


if __name__ == '__main__':
    main()
