from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def postorder(node: Optional[TreeNode]) -> tuple[int, Optional[TreeNode]]:
            if node is None:
                return 0, None

            left_depth, left_lca = postorder(node.left)
            right_depth, right_lca = postorder(node.right)

            if left_depth > right_depth:
                return left_depth + 1, left_lca
            elif right_depth > left_depth:
                return right_depth + 1, right_lca
            return left_depth + 1, node

        return postorder(root)[1]


def main():
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    assert Solution().lcaDeepestLeaves(root) == root.left.right

    root = TreeNode(1)
    assert Solution().lcaDeepestLeaves(root) == root

    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.left.right = TreeNode(2)
    assert Solution().lcaDeepestLeaves(root) == root.left.right


if __name__ == '__main__':
    main()
