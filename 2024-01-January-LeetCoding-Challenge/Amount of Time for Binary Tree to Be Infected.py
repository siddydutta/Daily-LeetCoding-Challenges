from collections import defaultdict
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # create undirected graph
        graph = defaultdict(list)
        def dfs(node: TreeNode) -> None:
            nonlocal graph
            if node.left is not None:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                dfs(node.left)
            if node.right is not None:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                dfs(node.right)
        dfs(root)

        minutes = 0
        current = [start]
        infected = {start}
        while current:
            neighbours = []
            for node in current:
                for neighbour in graph[node]:
                    if neighbour not in infected:
                        infected.add(neighbour)
                        neighbours.append(neighbour)
            if neighbours:
                minutes += 1
            current = neighbours
        return minutes


def main():
    root = TreeNode(1)
    root.left = TreeNode(5)
    root.right = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(6)
    root.left.right.left = TreeNode(9)
    root.left.right.right = TreeNode(2)
    start = 3
    assert Solution().amountOfTime(root, start) == 4

    root = TreeNode(1)
    start = 1
    assert Solution().amountOfTime(root, start) == 0


if __name__ == '__main__':
    main()
