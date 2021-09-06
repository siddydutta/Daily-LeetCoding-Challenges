# -*- coding: utf-8 -*-
from collections import defaultdict
from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        # Construct tree -> {node : [adjacent nodes]}
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        ans = [0] * n
        count = [1] * n  # Number of nodes in subtree i (node + children)

        def counter(node, parent):
            ''' Preorder DFS to count number of nodes in subtree '''
            for child in tree[node]:
                if child != parent:
                    counter(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]  # Count of children
        counter(0, -1)

        def add_rest(node, parent):
            ''' Postorder DFS to update distances '''
            for child in tree[node]:
                if child != parent:
                    # Count of child gets closer to node, while
                    # n - count of child goes further from node
                    ans[child] = ans[node] - count[child] + (n-count[child])
                    add_rest(child, node)
        add_rest(0, -1)
        return ans


def main():
    n = 6
    edges = [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]
    assert Solution().sumOfDistancesInTree(n, edges) == [8, 12, 6, 10, 10, 10]

    n = 1
    edges = []
    assert Solution().sumOfDistancesInTree(n, edges) == [0]

    n = 2
    edges = [[1, 0]]
    assert Solution().sumOfDistancesInTree(n, edges) == [1, 1]


if __name__ == '__main__':
    main()
