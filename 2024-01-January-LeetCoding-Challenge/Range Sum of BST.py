from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        queue = [root] if root else []
        range_sum = 0
        while queue:
            node = queue.pop(0)
            if low <= node.val <= high:
                range_sum += node.val
            if node.val > low and node.left is not None:
                queue.append(node.left)
            if node.val < high and node.right is not None:
                queue.append(node.right)
        return range_sum


def main():
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(18)
    low, high = 7, 15
    assert Solution().rangeSumBST(root, low, high) == 32

    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(18)
    root.left.left.left = TreeNode(1)
    root.left.right.left = TreeNode(6)
    low, high = 6, 10
    assert Solution().rangeSumBST(root, low, high) == 23


if __name__ == '__main__':
    main()
