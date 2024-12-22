from collections import defaultdict, deque
from typing import List


class Solution:
    def maxKDivisibleComponents(
        self, n: int, edges: List[List[int]], values: List[int], k: int
    ) -> int:
        if n <= 1:
            return 1

        count = 0
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        queue = deque(u for u, vs in graph.items() if len(vs) == 1)
        while queue:
            for _ in range(len(queue)):
                u = queue.popleft()
                p = next(iter(graph[u])) if graph[u] else -1

                if p >= 0:
                    graph[p].remove(u)

                if values[u] % k == 0:
                    count += 1
                else:
                    values[p] += values[u]

                if p >= 0 and len(graph[p]) == 1:
                    queue.append(p)

        return count


def main():
    n = 5
    edges = [[0, 2], [1, 2], [1, 3], [2, 4]]
    values = [1, 8, 1, 4, 4]
    k = 6
    assert Solution().maxKDivisibleComponents(n, edges, values, k) == 2

    n = 7
    edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]
    values = [3, 0, 6, 1, 5, 2, 1]
    k = 3
    assert Solution().maxKDivisibleComponents(n, edges, values, k) == 3


if __name__ == '__main__':
    main()
