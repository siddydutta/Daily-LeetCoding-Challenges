from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        tree = {-1: TreeNode()}  # dummy
        depth, value = 0, ''
        for ch in traversal + '-':
            if ch == '-' and value:
                parent = tree[depth - 1]
                child = TreeNode(int(value))
                if parent.left is None:
                    parent.left = child
                else:
                    parent.right = child
                tree[depth] = child
                depth = 1
                value = ''
            elif ch == '-':
                depth += 1
            else:
                value += ch
        return tree[-1].left


def main():
    traversal = '1-2--3--4-5--6--7'
    root = Solution().recoverFromPreorder(traversal)
    assert root.val == 1
    assert root.left.val == 2
    assert root.right.val == 5
    assert root.left.left.val == 3
    assert root.left.right.val == 4
    assert root.right.left.val == 6
    assert root.right.right.val == 7

    traversal = '1-2--3---4-5--6---7'
    root = Solution().recoverFromPreorder(traversal)
    assert root.val == 1
    assert root.left.val == 2
    assert root.right.val == 5
    assert root.left.left.val == 3
    assert root.left.left.left.val == 4
    assert root.right.left.val == 6
    assert root.right.left.left.val == 7

    traversal = '1-401--349---90--88'
    root = Solution().recoverFromPreorder(traversal)
    assert root.val == 1
    assert root.left.val == 401
    assert root.right is None
    assert root.left.left.val == 349
    assert root.left.right.val == 88
    assert root.left.left.left.val == 90


if __name__ == '__main__':
    main()
