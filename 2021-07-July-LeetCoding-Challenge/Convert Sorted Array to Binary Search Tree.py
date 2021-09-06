# -*- coding: utf-8 -*-
from typing import List


class TreeNode:
    ''' Definition for a binary tree node. '''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ''' Divide and conquer strategy using recursion. '''
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def addNodeToBST(start_index: int, end_index: int) -> TreeNode:
            if start_index > end_index:
                return None  # Base case
            mid_index = (start_index + end_index + 1) // 2
            root = TreeNode(nums[mid_index])
            root.left = addNodeToBST(start_index, mid_index-1)  # Left subtree
            root.right = addNodeToBST(mid_index+1, end_index)  # Right subtree
            return root

        root = addNodeToBST(0, len(nums)-1)
        return root


def main():
    nums = [-10, -3, 0, 5, 9]
    root = Solution().sortedArrayToBST(nums)
    assert root.val == 0
    assert root.left.val == -3
    assert root.right.val == 9
    assert root.left.left.val == -10
    assert not root.left.right
    assert root.right.left.val == 5
    assert not root.right.right


if __name__ == '__main__':
    main()
