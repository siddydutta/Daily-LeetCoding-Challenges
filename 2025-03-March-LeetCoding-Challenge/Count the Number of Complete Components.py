from collections import defaultdict


class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()

        def dfs(u: int) -> tuple[int, int]:
            nonlocal visited, graph
            visited.add(u)
            nodes, edges = 1, len(graph[u])
            for v in graph[u]:
                if v in visited:
                    continue
                sub_nodes, sub_edges = dfs(v)
                nodes += sub_nodes
                edges += sub_edges
            return nodes, edges

        completed = 0
        for node in range(n):
            if node in visited:
                continue
            nodes, edges = dfs(node)
            if nodes * (nodes - 1) == edges:
                completed += 1
        return completed


def main():
    n = 6
    edges = [[0, 1], [0, 2], [1, 2], [3, 4]]
    assert Solution().countCompleteComponents(n, edges) == 3

    n = 6
    edges = [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]]
    assert Solution().countCompleteComponents(n, edges) == 1


if __name__ == '__main__':
    main()
