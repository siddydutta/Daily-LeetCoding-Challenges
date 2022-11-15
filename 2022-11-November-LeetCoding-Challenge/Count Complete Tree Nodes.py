from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __get_depth(self, node: Optional[TreeNode]):
        if not node:
            return 0
        return 1 + self.__get_depth(node.left)  # Complete binary tree

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth = self.__get_depth(root.left)
        right_depth = self.__get_depth(root.right)
        if left_depth == right_depth:
            # Left sub tree is perfect binary tree
            # Right sub tree is complete binary tree
            return pow(2, left_depth) + self.countNodes(root.right)
        else:
            # Left sub tree is complete binary tree
            # Right sub tree is perfect binary tree
            return pow(2, right_depth) + self.countNodes(root.left)


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    assert Solution().countNodes(root) == 6

    root = None
    assert Solution().countNodes(root) == 0

    root = TreeNode(1)
    assert Solution().countNodes(root) == 1


if __name__ == '__main__':
    main()
