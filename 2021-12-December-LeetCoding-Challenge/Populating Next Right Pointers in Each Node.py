# -*- coding: utf-8 -*-
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None,
                 next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        ''' Depth-first search based solution. '''
        def dfs(node: Node, nextt: Node) -> None:
            if node is None:
                return  # Base case
            node.next = nextt  # Set the next for current node
            dfs(node.left, node.right)  # For a left child, set next to right
            # For a right node, set to parent's next's left child
            dfs(node.right, node.next.left if node.next is not None else None)

        dfs(root, None)
        return root


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    res = Solution().connect(root)
    assert res.next is None
    assert res.left.next == root.right
    assert res.right.next is None
    assert res.left.left.next == root.left.right
    assert res.left.right.next == root.right.left
    assert res.right.left.next == root.right.right
    assert res.right.right.next is None

    root = None
    assert Solution().connect(root) is None


if __name__ == '__main__':
    main()
