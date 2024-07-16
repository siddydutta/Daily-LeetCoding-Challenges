from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __find_lca(
            self, node: Optional[TreeNode], val1: int, val2: int
    ) -> Optional[TreeNode]:
        if node is None:
            return None
        if node.val == val1 or node.val == val2:
            return node
        left_lca = self.__find_lca(node.left, val1, val2)
        right_lca = self.__find_lca(node.right, val1, val2)
        if left_lca and right_lca:
            return node
        return left_lca if left_lca else right_lca

    def getDirections(
            self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        # only subtree from lowest common ancestor matters
        root = self.__find_lca(root, startValue, destValue)
        path_to_start, path_to_dest = '', ''

        # BFS to find path to start and dest
        stack = [(root, '')]
        while stack:
            node, path = stack.pop()
            if node.val == startValue:
                path_to_start = path
            if node.val == destValue:
                path_to_dest = path

            if node.left is not None:
                stack.append((node.left, path+'L'))
            if node.right is not None:
                stack.append((node.right, path+'R'))

        return 'U' * len(path_to_start) + path_to_dest


def main():
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(4)
    start_value = 3
    dest_value = 6
    assert Solution().getDirections(root, start_value, dest_value) == 'UURL'

    root = TreeNode(2)
    root.left = TreeNode(1)
    start_value = 2
    dest_value = 1
    assert Solution().getDirections(root, start_value, dest_value) == 'L'


if __name__ == '__main__':
    main()
