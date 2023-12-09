from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values, stack = list(), list()
        node = root
        while node is not None or stack:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            values.append(node.val)
            node = node.right
        return values


def main():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    assert Solution().inorderTraversal(root) == [1, 3, 2]

    assert not Solution().inorderTraversal(None)

    root = TreeNode(1)
    assert Solution().inorderTraversal(root) == [1]


if __name__ == '__main__':
    main()
