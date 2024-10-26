from collections import defaultdict
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeQueries(
            self, root: Optional[TreeNode], queries: List[int]
    ) -> List[int]:
        node_depth_map, node_height_map = defaultdict(int), defaultdict(int)
        level_nodes_map = defaultdict(list)

        def dfs(root: Optional[TreeNode], level: int = 0) -> int:
            if root is None:
                return -1
            nonlocal node_depth_map, level_nodes_map
            node_depth_map[root.val] = level
            level_nodes_map[level].append(root.val)
            height = max(dfs(root.left, level+1), dfs(root.right, level+1)) + 1
            node_height_map[root.val] = height
            return height

        dfs(root)
        cousin_height_map = defaultdict(lambda: [(0, None), (0, None)])
        for level, nodes in level_nodes_map.items():
            for node in nodes:
                height = node_height_map[node]
                if height >= cousin_height_map[level][0][0]:
                    cousin_height_map[level] = [(height, node),
                                                cousin_height_map[level][0]]
                elif height >= cousin_height_map[level][1][0]:
                    cousin_height_map[level] = [cousin_height_map[level][0],
                                                (height, node)]

        answer = []
        for query in queries:
            level = node_depth_map[query]
            max_height = level - 1
            for height, node in cousin_height_map[level]:
                if node != query:
                    max_height = max(max_height, node_depth_map[node]+height)
            answer.append(max_height)
        return answer


def main():
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(4)
    root.left.left = TreeNode(2)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    root.right.right.right = TreeNode(7)
    queries = [4]
    assert Solution().treeQueries(root, queries) == [2]

    root = TreeNode(5)
    root.left = TreeNode(8)
    root.right = TreeNode(9)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(7)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(6)
    queries = [3, 2, 4, 8]
    assert Solution().treeQueries(root, queries) == [3, 2, 3, 2]


if __name__ == '__main__':
    main()
