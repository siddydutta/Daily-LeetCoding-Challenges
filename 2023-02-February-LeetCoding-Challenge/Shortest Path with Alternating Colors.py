# -*- coding: utf-8 -*-
from math import inf
from typing import List


class Solution:
    def __build_graph(self, n: int, red_egdes: List[List[int]],
                      blue_edges: List[List[int]]) -> List[List[int]]:
        graph = [[[-n] for _ in range(n)] for _ in range(n)]
        for u, v in red_egdes:
            graph[u][v] = 1
        for u, v in blue_edges:
            if graph[u][v] == 1:
                graph[u][v] = 0
            else:
                graph[u][v] = -1
        return graph

    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]],
                                 blue_edges: List[List[int]]) -> List[int]:
        graph = self.__build_graph(n, red_edges, blue_edges)
        queue = [(0, 1), (0, -1)]
        result = [0] + [inf] * (n-1)
        path = 0
        visited = set()

        while queue:
            size = len(queue)
            path += 1
            for i in range(size):
                node, color = queue.pop(0)
                opp_color = -color
                for j in range(1, n):
                    if graph[node][j] == opp_color or graph[node][j] == 0:
                        if (j, opp_color) not in visited:
                            visited.add((j, opp_color))
                            queue.append((j, opp_color))
                            result[j] = min(result[j], path)

        return [i if i != inf else -1 for i in result]


def main():
    n = 3
    red_edges, blue_edges = [[0, 1], [1, 2]], []
    assert Solution().shortestAlternatingPaths(n, red_edges,
                                               blue_edges) == [0, 1, -1]

    n = 3
    red_edges, blue_edges = [[0, 1]], [[2, 1]]
    assert Solution().shortestAlternatingPaths(n, red_edges,
                                               blue_edges) == [0, 1, -1]


if __name__ == '__main__':
    main()
