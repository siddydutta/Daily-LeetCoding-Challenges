from collections import defaultdict, deque
from typing import List


class Solution:
    def __init__(self):
        self.graph = defaultdict(list)

    def __shortest_distance(self, n: int) -> int:
        queue = deque([(0, 0)])
        visited = set([0])

        while queue:
            node, distance = queue.popleft()
            if node == n-1:
                return distance
            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    queue.append((neighbour, distance + 1))
                    visited.add(neighbour)
        return -1

    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        for u in range(n-1):
            self.graph[u].append(u+1)

        result = []
        for u, v in queries:
            self.graph[u].append(v)
            result.append(self.__shortest_distance(n))
        return result


def main():
    n = 5
    queries = [[2, 4], [0, 2], [0, 4]]
    assert Solution().shortestDistanceAfterQueries(n, queries) == [3, 2, 1]

    n = 4
    queries = [[0, 3], [0, 2]]
    assert Solution().shortestDistanceAfterQueries(n, queries) == [1, 1]


if __name__ == '__main__':
    main()
