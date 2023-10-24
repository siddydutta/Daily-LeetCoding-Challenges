from math import inf
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = list()
        curr_level = [root] if root is not None else []
        while curr_level:
            curr_max = -inf
            next_level = list()
            for node in curr_level:
                curr_max = max(curr_max, node.val)
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            res.append(curr_max)
            curr_level = next_level
        return res


def main():
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(9)
    assert Solution().largestValues(root) == [1, 3, 9]

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert Solution().largestValues(root) == [1, 3]


if __name__ == '__main__':
    main()
