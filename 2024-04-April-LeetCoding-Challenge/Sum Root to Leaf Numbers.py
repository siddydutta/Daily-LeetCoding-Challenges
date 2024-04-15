from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total_sum = 0

        def dfs(node: Optional[TreeNode], number: str) -> None:
            if node is None:
                return
            number = f'{number}{node.val}'
            if node.left is None and node.right is None:
                nonlocal total_sum
                total_sum += int(number)
                return
            dfs(node.left, number)
            dfs(node.right, number)

        dfs(root, '')
        return total_sum


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
