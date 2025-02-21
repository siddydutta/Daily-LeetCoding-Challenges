from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.node_vals = set()

        def dfs(node: Optional[TreeNode], val: int) -> None:
            if node is None:
                return
            node.val = val
            self.node_vals.add(val)
            dfs(node.left, 2*val + 1)
            dfs(node.right, 2*val + 2)
        dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.node_vals


def main():
    root = TreeNode(-1)
    root.right = TreeNode(-1)
    obj = FindElements(root)
    assert obj.find(1) is False
    assert obj.find(2) is True


if __name__ == '__main__':
    main()
