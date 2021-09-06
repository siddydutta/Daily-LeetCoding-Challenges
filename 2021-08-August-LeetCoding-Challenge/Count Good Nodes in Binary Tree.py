# -*- coding: utf-8 -*-
class TreeNode:
    ''' Definition for a binary tree node. '''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    '''
    A node is a good node if it is greater or equal to the max value of all the
    nodes in the path taken from root to the node.
    DFS based solution.
    Time Complexity: O(n)
    '''
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, path_max_val: int) -> None:
            ''' Recursive DFS of binary tree. '''
            if not node:
                return
            self.count += node.val >= path_max_val  # Good node condition
            path_max_val = max(path_max_val, node.val)  # Update max
            if node.left:
                dfs(node.left, path_max_val)  # Explore left sub tree
            if node.right:
                dfs(node.right, path_max_val)  # Explore right sub tree

        self.count = 0
        dfs(root, root.val)
        return self.count


def main():
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(5)
    assert Solution().goodNodes(root) == 4

    root = TreeNode(3)
    root.left = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(2)
    assert Solution().goodNodes(root) == 3

    root = TreeNode(1)
    assert Solution().goodNodes(root) == 1


if __name__ == '__main__':
    main()
