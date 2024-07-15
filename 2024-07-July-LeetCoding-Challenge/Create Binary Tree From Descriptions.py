from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(
            self, descriptions: List[List[int]]
    ) -> Optional[TreeNode]:
        nodes = dict()
        children = set()
        for parent, child, is_left in descriptions:
            children.add(child)
            node = nodes.get(parent, TreeNode(parent))
            if is_left == 1:
                node.left = nodes.get(child, TreeNode(child))
                nodes[child] = node.left
            else:
                node.right = nodes.get(child, TreeNode(child))
                nodes[child] = node.right
            nodes[parent] = node

        for val in nodes.keys():
            if val not in children:
                return nodes[val]
        return None


def main():
    descriptions = [[20, 15, 1],
                    [20, 17, 0],
                    [50, 20, 1],
                    [50, 80, 0],
                    [80, 19, 1]]
    root = Solution().createBinaryTree(descriptions)
    assert root.val == 50
    assert root.left.val == 20
    assert root.right.val == 80
    assert root.left.left.val == 15
    assert root.left.right.val == 17
    assert root.right.left.val == 19
    assert root.right.right is None

    descriptions = [[1, 2, 1], [2, 3, 0], [3, 4, 1]]
    root = Solution().createBinaryTree(descriptions)
    assert root.val == 1
    assert root.left.val == 2
    assert root.right is None
    assert root.left.left is None
    assert root.left.right.val == 3
    assert root.left.right.left.val == 4
    assert root.left.right.right is None


if __name__ == '__main__':
    main()
