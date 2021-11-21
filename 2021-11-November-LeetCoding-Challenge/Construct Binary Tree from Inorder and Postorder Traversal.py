# -*- coding: utf-8 -*-
from typing import List


class TreeNode:
    ''' Definition for a binary tree node. '''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ''' Recursive, constant space solution. '''
    def buildTree(self, inorder: List[int], postorder: List[int]):
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        self.index = 1

        def build(left_idx: int, right_idx: int) -> TreeNode:
            if left_idx > right_idx:
                return
            # Since root is last in postorder, go reverse
            root = TreeNode(postorder[-self.index])
            self.index += 1
            root_idx = inorder_map.get(root.val)
            root.right = build(root_idx+1, right_idx)  # Right subtree
            root.left = build(left_idx, root_idx-1)  # Left subtree
            return root

        return build(0, len(inorder)-1)


def main():
    inorder, postorder = [9, 3, 15, 20, 7], [9, 15, 7, 20, 3]
    root = Solution().buildTree(inorder, postorder)
    assert root.val == 3
    assert root.left.val == 9
    assert root.right.val == 20
    assert root.right.left.val == 15
    assert root.right.right.val == 7

    inorder, postorder = [-1], [-1]
    root = Solution().buildTree(inorder, postorder)
    assert root.val == -1


if __name__ == '__main__':
    main()
