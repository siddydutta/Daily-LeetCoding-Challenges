# -*- coding: utf-8 -*-
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = [root] if root else []
        reverse, levels = False, []

        while queue:
            n, level = len(queue), []
            for _ in range(n):
                node = queue.pop(0)
                level.append(node.val)
                queue.extend(filter(None, [node.left, node.right]))
            levels.append(level[::-1]) if reverse else levels.append(level)
            reverse = not reverse

        return levels


def main():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert Solution().zigzagLevelOrder(root) == [[3], [20, 9], [15, 7]]

    root = TreeNode(1)
    assert Solution().zigzagLevelOrder(root) == [[1]]

    root = None
    assert Solution().zigzagLevelOrder(root) == []


if __name__ == '__main__':
    main()
