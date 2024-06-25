# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.sum = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        # reverse inorder traversal (right, root, left)
        if root.right is not None:
            self.bstToGst(root.right)
        self.sum += root.val
        root.val = self.sum
        if root.left is not None:
            self.bstToGst(root.left)
        return root


def main():
    root = TreeNode(4)
    root.left = TreeNode(1)
    root.right = TreeNode(6)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    root.left.right.right = TreeNode(3)
    root.right.right.right = TreeNode(8)
    result = Solution().bstToGst(root)
    assert result.val == 30
    assert result.left.val == 36
    assert result.right.val == 21
    assert result.left.left.val == 36
    assert result.left.right.val == 35
    assert result.right.left.val == 26
    assert result.right.right.val == 15
    assert result.left.right.right.val == 33
    assert result.right.right.right.val == 8

    root = TreeNode(0)
    root.right = TreeNode(1)
    result = Solution().bstToGst(root)
    assert result.val == 1
    assert result.right.val == 1


if __name__ == '__main__':
    main()
