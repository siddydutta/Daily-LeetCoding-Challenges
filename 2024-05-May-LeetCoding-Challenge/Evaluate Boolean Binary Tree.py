from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        def dfs(node: TreeNode) -> int:
            if not node.left and not node.right:
                return node.val
            left, right = map(dfs, (node.left, node.right))
            if node.val == 2:
                return left or right
            elif node.val == 3:
                return left and right

        return bool(dfs(root))


def main():
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(1)
    assert Solution().evaluateTree(root)

    root = TreeNode(0)
    assert not Solution().evaluateTree(root)


if __name__ == '__main__':
    main()
