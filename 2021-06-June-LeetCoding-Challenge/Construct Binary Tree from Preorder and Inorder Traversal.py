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
        self.elementIndex = dict()

    def buildSubTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # If no nodes to add
        if not preorder or not inorder:
            return None

        # Preorders first element is always root
        root = TreeNode(preorder[0])
        rootIndex = self.elementIndex.get(preorder[0])  # Minor optimization
        # Elements to the left of root index are left sub tree nodes
        root.left = self.buildTree(preorder[1:rootIndex+1],
                                   inorder[:rootIndex])
        # Elements to the right of root index are right sub tree nodes
        root.right = self.buildTree(preorder[rootIndex+1:],
                                    inorder[rootIndex+1:])
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # Hashmap to maintain element's indices in inorder traversal order
        self.elementIndex = {inorder[i]: i for i in range(len(inorder))}
        root = self.buildSubTree(preorder, inorder)
        return root


if __name__ == '__main__':
    obj = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = obj.buildTree(preorder, inorder)
    assert root.val == 3
    assert root.left.val == 9
    assert not root.left.left
    assert not root.left.right
    assert root.right.val == 20
    assert root.right.left.val == 15
    assert root.right.right.val == 7
    assert not root.right.left.left
    assert not root.right.left.right
    assert not root.right.right.left
    assert not root.right.right.right

    obj = Solution()
    preorder = [-1]
    inorder = [-1]
    root = obj.buildTree(preorder, inorder)
    assert root.val == -1
    assert not root.left
    assert not root.right
