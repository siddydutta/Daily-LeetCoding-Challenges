from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        queue1, queue2 = deque([root1]), deque([root2])
        while queue1 and queue2:
            node1, node2 = queue1.popleft(), queue2.popleft()
            if node1 is None or node2 is None:
                if node1 != node2:
                    return False
                continue
            if (node1.left == node2.left) or (getattr(node1.left, 'val', None) == getattr(node2.left, 'val', None)):
                queue1.extend([node1.left, node1.right])
            else:
                queue1.extend([node1.right, node1.left])  # flip
            queue2.extend([node2.left, node2.right])
        return queue1 == queue2


def main():
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    root1.right.left = TreeNode(6)
    root1.left.right.left = TreeNode(7)
    root1.left.right.right = TreeNode(8)
    root2 = TreeNode(1)
    root2.left = TreeNode(3)
    root2.right = TreeNode(2)
    root2.left.right = TreeNode(6)
    root2.right.left = TreeNode(4)
    root2.right.right = TreeNode(5)
    root2.right.right.left = TreeNode(8)
    root2.right.right.right = TreeNode(7)
    assert Solution().flipEquiv(root1, root2) is True

    root1 = None
    root2 = None
    assert Solution().flipEquiv(root1, root2) is True

    root1 = None
    root2 = TreeNode(1)
    assert Solution().flipEquiv(root1, root2) is False


if __name__ == '__main__':
    main()
