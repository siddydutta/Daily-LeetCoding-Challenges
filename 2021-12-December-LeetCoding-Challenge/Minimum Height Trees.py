# -*- coding: utf-8 -*-
from collections import defaultdict
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        ''' BFS based solution. '''
        if n == 1:
            return [0]

        neighbours = defaultdict(list)
        degrees = defaultdict(int)
        for u, v in edges:
            neighbours[u].append(v)
            neighbours[v].append(u)
            degrees[u] += 1
            degrees[v] += 1

        # Find leaves
        pre_level = list()
        unvisited = set(range(n))
        for i in range(n):
            if degrees[i] == 1:
                pre_level.append(i)

        while len(unvisited) > 2:
            curr_level = list()
            for u in pre_level:
                unvisited.remove(u)
                for v in neighbours[u]:
                    if v in unvisited:
                        degrees[v] -= 1
                        if degrees[v] == 1:
                            curr_level.append(v)
            pre_level = curr_level

        return pre_level


def main():
    n = 4
    edges = [[1, 0], [1, 2], [1, 3]]
    assert Solution().findMinHeightTrees(n, edges) == [1]

    n = 6
    edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
    assert Solution().findMinHeightTrees(n, edges) == [3, 4]

    n = 1
    edges = []
    assert Solution().findMinHeightTrees(n, edges) == [0]

    n = 2
    edges = [[0, 1]]
    assert Solution().findMinHeightTrees(n, edges) == [0, 1]


if __name__ == '__main__':
    main()
