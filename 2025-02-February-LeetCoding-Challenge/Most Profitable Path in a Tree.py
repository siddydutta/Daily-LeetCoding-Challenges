from collections import defaultdict
from typing import List


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs_bob(node: int) -> List[int]:
            if node == 0:
                return [node]
            nonlocal visited
            visited.add(node)
            path = []
            for neighbour in graph[node]:
                if neighbour not in visited:
                    path = dfs_bob(neighbour)
                    if path:
                        return [node] + path
        visited = set()
        bob_path = dfs_bob(bob)
        bob_visited_times = {node: i for i, node in enumerate(bob_path)}

        def dfs_alice(node: int, time: int) -> int:
            max_amount = float('-inf')
            nonlocal visited
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    max_amount = max(max_amount, dfs_alice(neighbour, time+1))
            vertex_income = amount[node]
            if bob_visited_times.get(node, float('inf')) < time:
                vertex_income = 0
            elif bob_visited_times.get(node, float('inf')) == time:
                vertex_income = amount[node] // 2
            if max_amount == float('-inf'):
                return vertex_income
            return max_amount + vertex_income

        visited = set()
        return dfs_alice(0, 0)


def main():
    edges = [[0, 1], [1, 2], [1, 3], [3, 4]]
    bob = 3
    amount = [-2, 4, 2, -4, 6]
    assert Solution().mostProfitablePath(edges, bob, amount) == 6

    edges = [[0, 1]]
    bob = 1
    amount = [-7280, 2350]
    assert Solution().mostProfitablePath(edges, bob, amount) == -7280


if __name__ == '__main__':
    main()
