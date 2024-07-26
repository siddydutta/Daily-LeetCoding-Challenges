from math import inf
from typing import List


class Solution:
    def findTheCity(
            self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        # create distance matrix
        # distance[u][v] = initial distance from node u to node v
        # inf if direct edge does not exist
        distance = [[inf]*n for _ in range(n)]
        for i in range(n):
            # distance to self node is 0
            distance[i][i] = 0
        for u, v, d in edges:
            # edges are not directed
            distance[u][v] = d
            distance[v][u] = d
        # compute min distance using floyd-warshall's algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distance[i][j] = min(distance[i][j],
                                         distance[i][k]+distance[k][j])

        # find min city
        min_cities, min_city = inf, None
        for city in range(n):
            cities = 0
            for idx, d in enumerate(distance[city]):
                # cities within threshold excluding self
                if idx != city and d <= distanceThreshold:
                    cities += 1
            if cities <= min_cities:
                # update min_city
                # city with greatest number in case of tie
                min_cities = cities
                min_city = city
        return min_city


def main():
    n = 4
    edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
    distanceThreshold = 4
    assert Solution().findTheCity(n, edges, distanceThreshold) == 3

    n = 5
    edges = [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]]
    distanceThreshold = 2
    assert Solution().findTheCity(n, edges, distanceThreshold) == 0


if __name__ == '__main__':
    main()
