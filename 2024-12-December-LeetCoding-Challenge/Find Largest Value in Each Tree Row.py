from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        level = deque([root] if root else [])
        while level:
            max_val = float('-inf')
            n_level = len(level)
            for _ in range(n_level):
                node = level.popleft()
                max_val = max(max_val, node.val)
                level.extend(filter(None, (node.left, node.right)))
            result.append(max_val)
        return result


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
