# -*- coding: utf-8 -*-
class TreeNode:
    ''' Definition for a binary tree node. '''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ''' DFS based solution. '''
    def sumNumbers(self, root: TreeNode) -> int:
        numbers = list()

        def dfs(root: TreeNode, number: int):
            if not root:
                return
            number = number * 10 + root.val
            if not root.left and not root.right:
                numbers.append(number)  # Leaf node condition
            dfs(root.left, number)
            dfs(root.right, number)

        dfs(root, 0)
        return sum(numbers)


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert Solution().sumNumbers(root) == 25

    root = TreeNode(4)
    root.left = TreeNode(9)
    root.right = TreeNode(0)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(1)
    assert Solution().sumNumbers(root) == 1026


if __name__ == '__main__':
    main()
