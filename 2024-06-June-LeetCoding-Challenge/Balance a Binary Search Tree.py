from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        values = []

        # Inorder traversal
        def inorder(node: TreeNode) -> None:
            if node:
                inorder(node.left)
                values.append(node.val)
                inorder(node.right)
        inorder(root)

        # Construct a balanced BST
        def bst(nodes: List[int]) -> Optional[TreeNode]:
            if not nodes:
                return None
            mid = len(nodes) // 2
            root = TreeNode(val=nodes[mid])
            root.left = bst(nodes[:mid])
            root.right = bst(nodes[mid+1:])
            return root

        return bst(values)


def main():
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    result = Solution().balanceBST(root)
    assert result.val == 3
    assert result.left.val == 2
    assert result.right.val == 4
    assert result.left.left.val == 1

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    result = Solution().balanceBST(root)
    assert result.val == 2
    assert result.left.val == 1
    assert result.right.val == 3


if __name__ == '__main__':
    main()
