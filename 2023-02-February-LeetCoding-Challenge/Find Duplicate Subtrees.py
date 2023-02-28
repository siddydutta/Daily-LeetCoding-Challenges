# -*- coding: utf-8 -*-
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        hashmap = {}
        self.solve(root, hashmap)
        return [node for val, node in hashmap.values() if val > 1]

    def solve(self, root: Optional[TreeNode], hashmap: dict) -> str:
        if not root:
            return None
        left = self.solve(root.left, hashmap)
        right = self.solve(root.right, hashmap)
        temp = f'{root.val} {left} {right}'
        if temp not in hashmap:
            hashmap[temp] = [1, root]
        else:
            hashmap[temp][0] += 1
        return temp


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(4)
    root.right.left.left = TreeNode(4)
    solution = Solution().findDuplicateSubtrees(root)
    assert len(solution) == 2
    assert solution[0].val == 4
    assert solution[1].val == 2

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    solution = Solution().findDuplicateSubtrees(root)
    assert len(solution) == 1
    assert solution[0].val == 1

    root = TreeNode(2)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(3)
    solution = Solution().findDuplicateSubtrees(root)
    assert len(solution) == 2
    assert solution[0].val == 3
    assert solution[1].val == 2


if __name__ == '__main__':
    main()
