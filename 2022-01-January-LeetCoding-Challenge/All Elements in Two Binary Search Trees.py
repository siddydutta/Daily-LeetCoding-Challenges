# -*- coding: utf-8 -*-
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.__elements = list()

    def __inorder(self, node: TreeNode) -> None:
        ''' Perform inorder traversal and add elements to list. '''
        if not node:
            return
        self.__inorder(node.left)
        self.__elements.append(node.val)
        self.__inorder(node.right)

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ''' Straightforward inorder traversal based solution. '''
        self.__inorder(root1), self.__inorder(root2)
        self.__elements.sort()
        return self.__elements


def main():
    root1 = TreeNode(2)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root2 = TreeNode(1)
    root2.left = TreeNode(0)
    root2.right = TreeNode(3)
    assert Solution().getAllElements(root1, root2) == [0, 1, 1, 2, 3, 4]

    root1 = TreeNode(1)
    root1.right = TreeNode(8)
    root2 = TreeNode(8)
    root2.left = TreeNode(1)
    assert Solution().getAllElements(root1, root2) == [1, 1, 8, 8]


if __name__ == '__main__':
    main()
