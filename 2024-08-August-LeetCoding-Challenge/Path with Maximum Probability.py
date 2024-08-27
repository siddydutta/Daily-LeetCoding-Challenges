from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
    def maxProbability(
            self, n: int,
            edges: List[List[int]],
            succProb: List[float],
            start_node: int,
            end_node: int
    ) -> float:
        # represent graph as adjacency list
        graph = defaultdict(list)
        for (u, v), p in zip(edges, succProb):
            graph[u].append((v, p))
            graph[v].append((u, p))

        # dijkstra's algorithm to calculate max probabilities
        max_heap = [(-1, start_node)]  # for max probability
        max_prob = [0.0 if i != start_node else 1.0 for i in range(n)]
        while max_heap:
            curr_prob, node = heappop(max_heap)
            curr_prob = -curr_prob

            for neighbour, prob in graph[node]:
                new_prob = curr_prob * prob
                if new_prob > max_prob[neighbour]:
                    max_prob[neighbour] = new_prob
                    heappush(max_heap, (-new_prob, neighbour))

        return max_prob[end_node]


def main():
    n = 3
    edges = [[0, 1], [1, 2], [0, 2]]
    succProb = [0.5, 0.5, 0.2]
    start = 0
    end = 2
    assert Solution().maxProbability(n, edges, succProb, start, end) == 0.25

    n = 3
    edges = [[0, 1], [1, 2], [0, 2]]
    succProb = [0.5, 0.5, 0.3]
    start = 0
    end = 2
    assert Solution().maxProbability(n, edges, succProb, start, end) == 0.3

    n = 3
    edges = [[0, 1]]
    succProb = [0.5]
    start = 0
    end = 2
    assert Solution().maxProbability(n, edges, succProb, start, end) == 0.0


if __name__ == '__main__':
    main()
