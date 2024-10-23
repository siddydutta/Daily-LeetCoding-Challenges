from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(
            self, root: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        queue = deque([root])
        root.val = 0
        while queue:
            curr_level, next_level = [], deque([])
            level_sum = 0
            while queue:
                node = queue.popleft()
                curr_level.append(node)
                for child in filter(None, (node.left, node.right)):
                    level_sum += child.val
                    next_level.append(child)
            queue = next_level
            for node in curr_level:
                cousin_sum = level_sum
                for child in filter(None, (node.left, node.right)):
                    cousin_sum -= child.val
                for child in filter(None, (node.left, node.right)):
                    child.val = cousin_sum
        return root


def main():
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(9)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(10)
    root.right.right = TreeNode(7)
    result = Solution().replaceValueInTree(root)
    assert result.val == 0
    assert result.left.val == 0
    assert result.right.val == 0
    assert result.left.left.val == 7
    assert result.left.right.val == 7
    assert result.right.right.val == 11

    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    result = Solution().replaceValueInTree(root)
    assert result.val == 0
    assert result.left.val == 0
    assert result.right.val == 0


if __name__ == '__main__':
    main()
