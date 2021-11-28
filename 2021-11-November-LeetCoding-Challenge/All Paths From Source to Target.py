# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ''' Depth first search solution. '''
        n, paths = len(graph), list()

        def dfs(path):
            if path[-1] == n-1:
                # If last node in path is last node
                nonlocal paths
                paths.append(path)
                return

            for next_node in graph[path[-1]]:
                # Traverse through each possible node
                dfs(path+[next_node])

        dfs([0])  # Start from node 0
        return paths


def main():
    graph = [[1, 2], [3], [3], []]
    assert Solution().allPathsSourceTarget(graph) == [[0, 1, 3], [0, 2, 3]]

    graph = [[4, 3, 1], [3, 2, 4], [3], [4], []]
    assert Solution().allPathsSourceTarget(graph) == [[0, 4], [0, 3, 4],
                                                      [0, 1, 3, 4],
                                                      [0, 1, 2, 3, 4],
                                                      [0, 1, 4]]

    graph = [[1], []]
    assert Solution().allPathsSourceTarget(graph) == [[0, 1]]

    graph = [[1, 2, 3], [2], [3], []]
    assert Solution().allPathsSourceTarget(graph) == [[0, 1, 2, 3], [0, 2, 3],
                                                      [0, 3]]

    graph = [[1, 3], [2], [3], []]
    assert Solution().allPathsSourceTarget(graph) == [[0, 1, 2, 3], [0, 3]]


if __name__ == '__main__':
    main()
