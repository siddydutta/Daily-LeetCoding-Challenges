class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.weights = [-1] * n

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int, weight: int) -> None:
        xx, yy = self.find(x), self.find(y)
        if self.rank[xx] < self.rank[yy]:
            self.parent[xx] = yy
        else:
            self.parent[yy] = xx

        self.weights[xx] = self.weights[yy] = self.weights[xx] & self.weights[yy] & weight
        if self.rank[xx] == self.rank[yy]:
            self.rank[xx] += 1

    def minimum_cost_of_walk(self, x: int, y: int) -> int:
        if x == y:
            return 0
        if self.find(x) != self.find(y):
            return -1
        return self.weights[self.find(x)]


class Solution:
    def minimumCost(self, n: int, edges: list[list[int]], query: list[list[int]]) -> list[int]:
        uf = UnionFind(n)
        for u, v, w in edges:
            uf.union(u, v, w)
        return [uf.minimum_cost_of_walk(u, v) for u, v in query]


def main():
    n = 5
    edges = [[0, 1, 7], [1, 3, 7], [1, 2, 1]]
    query = [[0, 3], [3, 4]]
    assert Solution().minimumCost(n, edges, query) == [1, -1]

    n = 3
    edges = [[0, 2, 7], [0, 1, 15], [1, 2, 6], [1, 2, 1]]
    query = [[1, 2]]
    assert Solution().minimumCost(n, edges, query) == [0]


if __name__ == '__main__':
    main()
