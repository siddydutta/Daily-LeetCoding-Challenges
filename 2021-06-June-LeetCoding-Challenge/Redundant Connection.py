# -*- coding: utf-8 -*-
from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n+1)]

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> None:
        self.parent[self.find(x)] = self.find(y)


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for i, j in edges:
            if uf.find(i) == uf.find(j):
                return [i, j]
            else:
                uf.union(i, j)
        return None


def main():
    obj = Solution()

    edges = [[1, 2], [1, 3], [2, 3]]
    assert obj.findRedundantConnection(edges) == [2, 3]

    edges = [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    assert obj.findRedundantConnection(edges) == [1, 4]


if __name__ == '__main__':
    main()
