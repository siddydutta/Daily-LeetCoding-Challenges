from collections import defaultdict
from math import inf
from typing import List


class Solution:
    def secondMinimum(
            self, n: int, edges: List[List[int]], time: int, change: int
    ) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        dis1, dis2 = [inf]*(n+1), [inf]*(n+1)
        dis1[1] = 0
        queue = [(1, 0)]
        while queue:
            node, cost = queue.pop(0)
            for neighbour in graph[node]:
                new_cost = cost + time
                if (cost // change) % 2 == 1:
                    new_cost += change - (cost % change)

                if dis1[neighbour] > new_cost:
                    dis2[neighbour], dis1[neighbour] = dis1[neighbour], new_cost
                    queue.append((neighbour, new_cost))
                elif new_cost > dis1[neighbour] and new_cost < dis2[neighbour]:
                    dis2[neighbour] = new_cost
                    queue.append((neighbour, new_cost))
        return dis2[n]


def main():
    n = 5
    edges = [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]]
    time = 3
    change = 5
    assert Solution().secondMinimum(n, edges, time, change) == 13

    n = 2
    edges = [[1, 2]]
    time = 3
    change = 2
    assert Solution().secondMinimum(n, edges, time, change) == 11


if __name__ == '__main__':
    main()
