from typing import Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0
        def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
            if node is None:
                return 0, 0
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1
            if total_sum // total_count == node.val:
                nonlocal count
                count += 1
            return total_sum, total_count
        dfs(root)
        return count


def main():
    root = TreeNode(4)
    root.left = TreeNode(8)
    root.right = TreeNode(5)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)
    root.right.right = TreeNode(6)
    assert Solution().averageOfSubtree(root) == 5


    root = TreeNode(1)
    assert Solution().averageOfSubtree(root) == 1


if __name__ == '__main__':
    main()
