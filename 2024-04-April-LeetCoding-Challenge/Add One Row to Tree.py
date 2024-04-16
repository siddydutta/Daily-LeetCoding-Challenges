# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth == 1:
            # boundary condition
            return TreeNode(val=val, left=root)

        queue = [root]
        level = 1
        # navigate to level == depth-1
        while level < depth-1:
            for _ in range(len(queue)):
                node = queue.pop(0)
                queue.extend(filter(None, (node.left, node.right)))
            level += 1

        # add one row
        while queue:
            node = queue.pop(0)
            node.left = TreeNode(val=val, left=node.left)
            node.right = TreeNode(val=val, right=node.right)
        return root


def main():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(5)
    root = Solution().addOneRow(root, 1, 2)
    assert root.val == 4
    assert root.left.val == 1
    assert root.right.val == 1
    assert root.left.left.val == 2
    assert root.left.right is None
    assert root.right.left is None
    assert root.right.right.val == 6
    assert root.left.left.left.val == 3
    assert root.left.left.right.val == 1
    assert root.right.right.left.val == 5
    assert root.right.right.right is None

    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(1)
    root = Solution().addOneRow(root, 1, 3)
    assert root.val == 4
    assert root.left.val == 2
    assert root.right is None
    assert root.left.left.val == 1
    assert root.left.right.val == 1
    assert root.left.left.left.val == 3
    assert root.left.left.right is None
    assert root.left.right.left is None
    assert root.left.right.right.val == 1


if __name__ == '__main__':
    main()
