# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        # Create adjacency matrix
        graph = [[None for _ in range(n)] for _ in range(n)]
        for u, v, cnt in edges:
            graph[u][v] = cnt
            graph[v][u] = cnt

        ans = 0
        visited = [None for _ in range(n)]
        return


def main():
    edges = [[0, 1, 10], [0, 2, 1], [1, 2, 2]]
    maxMoves = 6
    n = 3
    assert Solution().reachableNodes(edges, maxMoves, n) == 13

    edges = [[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1]]
    maxMoves = 10
    n = 4
    assert Solution().reachableNodes(edges, maxMoves, n) == 23

    edges = [[1, 2, 4], [1, 4, 5], [1, 3, 1], [2, 3, 4], [3, 4, 5]]
    maxMoves = 17
    n = 5
    assert Solution().reachableNodes(edges, maxMoves, n) == 1


if __name__ == '__main__':
    main()
