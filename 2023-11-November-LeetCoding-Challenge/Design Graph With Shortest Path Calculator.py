from heapq import heappush, heappop
from typing import List


class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.adjacency_list = [[] for _ in range(n)]
        for u, v, cost in edges:
            self.adjacency_list[u].append((v, cost))

    def addEdge(self, edge: List[int]) -> None:
        self.adjacency_list[edge[0]].append((edge[1], edge[2]))

    def shortestPath(self, node1: int, node2: int) -> int:
        visited = set()
        queue = [(0, node1)]
        while queue:
            distance, node = heappop(queue)
            if node == node2:
                return distance
            if node in visited:
                continue
            visited.add(node)
            for neighbor, cost in self.adjacency_list[node]:
                if neighbor not in visited:
                    heappush(queue, (distance + cost, neighbor))
        return -1


def main():
    n = 4
    edges = [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]
    obj = Graph(n, edges)
    assert obj.shortestPath(3, 2) == 6
    assert obj.shortestPath(0, 3) == -1
    obj.addEdge([1, 3, 4])
    assert obj.shortestPath(0, 3) == 6


if __name__ == '__main__':
    main()
