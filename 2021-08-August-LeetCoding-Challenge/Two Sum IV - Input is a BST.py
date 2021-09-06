# -*- coding: utf-8 -*-
from collections import deque
from typing import Optional


class TreeNode:
    ''' Definition for a binary tree node. '''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution2:
    ''' DFS using BST properties. '''
    def search(self, root: TreeNode, current: TreeNode, val: int) -> bool:
        if not root:
            return False
        return root.val == val and root != current or \
            root.val < val and self.search(root.right, current, val) or \
            root.val > val and self.search(root.left, current, val)

    def dfs(self, root: TreeNode, current: TreeNode, k: int) -> bool:
        if not current:
            return False
        return self.search(root, current, k - current.val) or \
            self.dfs(root, current.left, k) or \
            self.dfs(root, current.right, k)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        return self.dfs(root, root, k)


class Solution1:
    ''' Straightforward BFS Solution. '''
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        visited = set()
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if k - node.val in visited:
                return True
            visited.add(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False


class Solution:
    ''' Straightforward DFS Solution. '''
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        def dfs(node: TreeNode) -> None:
            if not node:
                return False
            if k - node.val in visited:
                return True
            visited.add(node.val)
            return dfs(node.left) or dfs(node.right)

        visited = set()
        return dfs(root)


def main():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)
    k = 9
    assert Solution().findTarget(root, k)

    k = 28
    assert not Solution().findTarget(root, k)

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    k = 4
    assert Solution().findTarget(root, k)

    k = 1
    assert not Solution().findTarget(root, k)

    k = 3
    assert Solution().findTarget(root, k)


if __name__ == '__main__':
    main()
