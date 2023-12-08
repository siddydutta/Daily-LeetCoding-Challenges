from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            nonlocal string
            if node.left is None and node.right is None:
                string += str(node.val)
                return

            string += str(node.val)
            string += '('
            dfs(node.left)
            string += ')'
            if node.right:
                string += '('
                dfs(node.right)
                string += ')'

        string = ''
        dfs(root)
        return string


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    assert Solution().tree2str(root) == '1(2(4))(3)'

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    assert Solution().tree2str(root) == '1(2()(4))(3)'


if __name__ == '__main__':
    main()
