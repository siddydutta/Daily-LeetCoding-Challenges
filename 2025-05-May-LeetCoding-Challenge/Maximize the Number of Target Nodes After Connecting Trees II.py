from collections import deque


class Solution:
    def __init__(self):
        self.even_1, self.odd_1 = 0, 0
        self.even_2, self.odd_2 = 0, 0

    def __build_adj_list(self, edges: list[list[int]]) -> list[list[int]]:
        n = len(edges) + 1
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph

    def __bfs_colour(self, graph: list[list[int]], colour: list[int], flag: bool):
        queue = deque([0])
        colour[0] = 0
        while queue:
            u = queue.popleft()
            if colour[u] == 0:
                if flag:
                    self.even_1 += 1
                else:
                    self.even_2 += 1
            else:
                if flag:
                    self.odd_1 += 1
                else:
                    self.odd_2 += 1
            for v in graph[u]:
                if colour[v] == -1:
                    colour[v] = colour[u] ^ 1
                    queue.append(v)

    def maxTargetNodes(self, edges1: list[list[int]], edges2: list[list[int]]) -> list[int]:
        graph1, graph2 = map(self.__build_adj_list, (edges1, edges2))
        colour_1, colour_2 = [-1] * len(graph1), [-1] * len(graph2)
        self.__bfs_colour(graph1, colour_1, True)
        self.__bfs_colour(graph2, colour_2, False)
        max_target2 = max(self.even_2, self.odd_2)
        return [(self.even_1 if colour_1[node] == 0 else self.odd_1) + max_target2
                for node in range(len(graph1))]


def main():
    edges1 = [[0, 1], [0, 2], [2, 3], [2, 4]]
    edges2 = [[0, 1], [0, 2], [0, 3], [2, 7], [1, 4], [4, 5], [4, 6]]
    assert Solution().maxTargetNodes(edges1, edges2) == [8, 7, 7, 8, 8]

    edges1 = [[0, 1], [0, 2], [0, 3], [0, 4]]
    edges2 = [[0, 1], [1, 2], [2, 3]]
    assert Solution().maxTargetNodes(edges1, edges2) == [3, 6, 6, 6, 6]


if __name__ == '__main__':
    main()
