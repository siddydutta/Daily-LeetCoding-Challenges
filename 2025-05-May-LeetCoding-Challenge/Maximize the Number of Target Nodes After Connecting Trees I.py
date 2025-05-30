from collections import deque


class Solution:
    def __build_adj_list(self, edges: list[list[int]]) -> list[list[int]]:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph

    def __bfs(self, graph: list[list[int]], start: int, k: int) -> int:
        level = 0
        queue = deque([start])
        visited = {start}
        count = 1  # node is always target to itself
        while queue and level < k:
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbour in graph[node]:
                    if neighbour not in visited:
                        count += 1
                        visited.add(neighbour)
                        queue.append(neighbour)
            level += 1
        return count

    def maxTargetNodes(
        self, edges1: list[list[int]], edges2: list[list[int]], k: int
    ) -> list[int]:
        graph1, graph2 = map(self.__build_adj_list, (edges1, edges2))
        n_targets1 = [self.__bfs(graph1, node, k) for node in range(len(graph1))]
        max_targets2 = 0
        if k > 0:
            for node in range(len(graph2)):
                max_targets2 = max(max_targets2, self.__bfs(graph2, node, k - 1))
        return [n_targets + max_targets2 for n_targets in n_targets1]


def main():
    edges1 = [[0, 1], [0, 2], [2, 3], [2, 4]]
    edges2 = [[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]]
    k = 2
    assert Solution().maxTargetNodes(edges1, edges2, k) == [9, 7, 9, 8, 8]

    edges1 = [[0, 1], [0, 2], [0, 3], [0, 4]]
    edges2 = [[0, 1], [1, 2], [2, 3]]
    k = 1
    assert Solution().maxTargetNodes(edges1, edges2, k) == [6, 3, 3, 3, 3]


if __name__ == '__main__':
    main()
