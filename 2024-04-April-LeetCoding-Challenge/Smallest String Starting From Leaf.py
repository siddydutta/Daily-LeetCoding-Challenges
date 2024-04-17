from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        min_string = None

        def dfs(node: Optional[TreeNode], string: str = '') -> None:
            if node is None:
                return
            string += chr(node.val + 97)
            if node.left is None and node.right is None:
                nonlocal min_string
                if min_string is None:
                    min_string = string[::-1]
                else:
                    min_string = min(min_string, string[::-1])
            dfs(node.left, string)
            dfs(node.right, string)

        dfs(root)
        return min_string


def main():
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(4)
    assert Solution().smallestFromLeaf(root) == 'dba'

    root = TreeNode(25)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(2)
    assert Solution().smallestFromLeaf(root) == 'adz'

    root = TreeNode(2)
    root.left = TreeNode(2)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(0)
    assert Solution().smallestFromLeaf(root) == 'abc'


if __name__ == '__main__':
    main()
