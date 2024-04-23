from collections import defaultdict
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        # create adjacency matrix
        neighbours = defaultdict(set)
        for u, v in edges:
            neighbours[u].add(v)
            neighbours[v].add(u)

        # repeatedly remove leaf nodes until possible MTHs
        leaves = [u for u in range(n) if len(neighbours[u]) == 1]
        while n > 2:
            n -= len(leaves)
            next_leaves = []
            for u in leaves:
                # leaf node will have one neighbour
                v = neighbours[u].pop()
                # remove leaf node link
                neighbours[v].remove(u)
                if len(neighbours[v]) == 1:
                    # is a new leaf node
                    next_leaves.append(v)
            leaves = next_leaves
        return leaves


def main():
    n = 4
    edges = [[1, 0], [1, 2], [1, 3]]
    assert Solution().findMinHeightTrees(n, edges) == [1]

    n = 6
    edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
    assert Solution().findMinHeightTrees(n, edges) == [3, 4]


if __name__ == '__main__':
    main()
