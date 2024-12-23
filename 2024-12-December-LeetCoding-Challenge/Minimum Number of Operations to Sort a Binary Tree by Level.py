from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _get_min_swaps(self, level_vals):
        swaps = 0
        idx_map = {val: idx for idx, val in enumerate(level_vals)}
        sorted_vals = sorted(level_vals)

        for i in range(len(level_vals)):
            if level_vals[i] == sorted_vals[i]:
                continue
            swaps += 1
            cur_pos = idx_map[sorted_vals[i]]
            idx_map[level_vals[i]] = cur_pos
            level_vals[cur_pos] = level_vals[i]
        return swaps

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        ops = 0
        while queue:
            level_vals = [node.val for node in queue]
            ops += self._get_min_swaps(level_vals)
            queue = [child for node in queue
                     for child in filter(None, (node.left, node.right))]
        return ops


def main():
    root = TreeNode(1)
    root.left = TreeNode(4)
    root.right = TreeNode(3)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(6)
    root.right.left = TreeNode(8)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(9)
    root.right.right.left = TreeNode(10)
    assert Solution().minimumOperations(root) == 3

    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.left.left = TreeNode(7)
    root.left.right = TreeNode(6)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(4)
    assert Solution().minimumOperations(root) == 3

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    assert Solution().minimumOperations(root) == 0


if __name__ == '__main__':
    main()
