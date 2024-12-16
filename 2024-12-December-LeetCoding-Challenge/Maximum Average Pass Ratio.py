from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def maxAverageRatio(
            self, classes: List[List[int]], extraStudents: int
    ) -> float:
        def profit(a, b):
            return (a + 1) / (b + 1) - a / b

        max_heap = []
        for a, b in classes:
            max_heap.append((-profit(a, b), a, b))
        heapify(max_heap)

        for _ in range(extraStudents):
            _, a, b = heappop(max_heap)
            heappush(max_heap, (-profit(a + 1, b + 1), a + 1, b + 1))

        return sum(a / b for _, a, b in max_heap) / len(classes)


def main():
    classes = [[1, 2], [3, 5], [2, 2]]
    extraStudents = 2
    result = Solution().maxAverageRatio(classes, extraStudents)
    assert abs(result - 0.78333) < 1e-5

    classes = [[2, 4], [3, 9], [4, 5], [2, 10]]
    extraStudents = 4
    result = Solution().maxAverageRatio(classes, extraStudents)
    assert abs(result - 0.53485) < 1e-5


if __name__ == '__main__':
    main()
