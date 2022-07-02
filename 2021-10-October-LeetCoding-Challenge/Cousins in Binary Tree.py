# -*- coding: utf-8 -*-
from typing import Optional


class TreeNode:
    ''' Definition for a binary tree node. '''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ''' Breadth first search solution. '''
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = [root]
        while queue:
            n = len(queue)
            is_x, is_y = False, False
            # Traverse every level
            for _ in range(n):
                node = queue.pop(0)
                # Update flags if found in the level
                if node.val == x:
                    is_x = True
                if node.val == y:
                    is_y = True

                # Check if cousins have the same parent
                if node.left and node.right:
                    if (node.left.val == x and node.right.val == y) or \
                    (node.left.val == y and node.right.val == x):
                        return False

                # Level order traversal
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if is_x and is_y:
                return True  # Both x, y are on the same level
            if is_x or is_y:
                return False  # Either x, y are present (since unique)
        return False


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    x, y = 4, 3
    assert not Solution().isCousins(root, x, y)

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(5)
    x, y = 5, 4
    assert Solution().isCousins(root, x, y)


if __name__ == '__main__':
    main()
