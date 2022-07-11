from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue, values = [root] if root else list(), list()
        while queue:
            node, level = queue[0], list()
            while queue:
                node = queue.pop(0)
                level += filter(None, [node.left, node.right])
            values.append(node.val)
            queue = level
        return values


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    assert Solution().rightSideView(root) == [1, 3, 4]

    root = TreeNode(1, TreeNode(2))
    assert Solution().rightSideView(root) == [1, 2]


if __name__ == '__main__':
    main()
