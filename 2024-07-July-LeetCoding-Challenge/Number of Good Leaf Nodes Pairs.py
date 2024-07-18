from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        count = 0

        def dfs(node: TreeNode) -> List[int]:
            if node is None:
                return []
            if node.left is None and node.right is None:
                return [1]  # leaf node

            # post-order dfs
            left_list, right_list = dfs(node.left), dfs(node.right)
            nonlocal count
            for left_dist in left_list:
                for right_dist in right_list:
                    count += bool(left_dist+right_dist <= distance)
            # distance from current node to leaf node
            return [1+item for item in left_list+right_list]

        dfs(root)
        return count


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    assert Solution().countPairs(root, 3) == 1

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    assert Solution().countPairs(root, 3) == 2


if __name__ == '__main__':
    main()
