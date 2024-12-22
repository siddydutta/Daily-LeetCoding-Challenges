from heapq import heappush, heappop
from typing import List


class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        max_idx = []
        results = [-1] * len(queries)
        store_queries = [[] for _ in heights]

        for idx, (a, b) in enumerate(queries):
            if a < b and heights[a] < heights[b]:
                results[idx] = b
            elif a > b and heights[a] > heights[b]:
                results[idx] = a
            elif a == b:
                results[idx] = a
            else:
                store_queries[max(a, b)].append(
                    (max(heights[a], heights[b]), idx)
                )

        for idx, height in enumerate(heights):
            while max_idx and max_idx[0][0] < height:
                _, q_idx = heappop(max_idx)
                results[q_idx] = idx
            for element in store_queries[idx]:
                heappush(max_idx, element)

        return results


def main():
    heights = [6, 4, 8, 5, 2, 7]
    queries = [[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]]
    assert Solution().leftmostBuildingQueries(heights, queries) == [2, 5, -1, 5, 2]

    heights = [5, 3, 8, 2, 6, 1, 4, 6]
    queries = [[0, 7], [3, 5], [5, 2], [3, 0], [1, 6]]
    assert Solution().leftmostBuildingQueries(heights, queries) == [7, 6, -1, 4, 6]


if __name__ == '__main__':
    main()
