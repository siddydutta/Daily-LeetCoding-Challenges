from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        total_sum = 0
        while queue:
            next_queue = []
            for node in queue:
                if node.left:
                    if not node.left.left and not node.left.right:
                        total_sum += node.left.val
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue
        return total_sum


def main():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert Solution().sumOfLeftLeaves(root) == 24

    root = TreeNode(1)
    assert Solution().sumOfLeftLeaves(root) == 0


if __name__ == '__main__':
    main()
