from collections import deque
from math import ceil
from typing import List, Tuple


class Solution:
    def __build_adj_list(self, n: int, edges: List[int]) -> List[List[int]]:
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        return adj_list

    def __find_diameter(self, n: int, adj_list: List[List[int]]) -> int:
        farthest_node, _ = self.__find_farthest_node(n, adj_list)
        _, diameter = self.__find_farthest_node(n, adj_list, farthest_node)
        return diameter

    def __find_farthest_node(
            self, n: int, adj_list: List[List[int]], source_node: int = 0
    ) -> Tuple[int, int]:
        queue = deque([source_node])
        visited = [i == source_node for i in range(n)]

        max_distance = 0
        farthest_node = source_node

        while queue:
            for _ in range(len(queue)):
                current_node = queue.popleft()
                farthest_node = current_node
                for neighbor in adj_list[current_node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            if queue:
                max_distance += 1

        return farthest_node, max_distance

    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        n, m = len(edges1) + 1, len(edges2) + 1

        adj_list1 = self.__build_adj_list(n, edges1)
        adj_list2 = self.__build_adj_list(m, edges2)

        diameter1 = self.__find_diameter(n, adj_list1)
        diameter2 = self.__find_diameter(m, adj_list2)

        combined_diameter = ceil(diameter1 / 2) + ceil(diameter2 / 2) + 1
        return max(diameter1, diameter2, combined_diameter)


def main():
    edges1 = [[0, 1], [0, 2], [0, 3]]
    edges2 = [[0, 1]]
    assert Solution().minimumDiameterAfterMerge(edges1, edges2) == 3

    edges1 = [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]]
    edges2 = [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6], [2, 7]]
    assert Solution().minimumDiameterAfterMerge(edges1, edges2) == 5


if __name__ == '__main__':
    main()
