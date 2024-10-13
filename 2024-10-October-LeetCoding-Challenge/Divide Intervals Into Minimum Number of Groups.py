from heapq import heappop, heappush
from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        heap = []
        for start, end in sorted(intervals):
            if heap and heap[0] < start:
                heappop(heap)
            heappush(heap, end)
        return len(heap)


def main():
    intervals = [[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]
    assert Solution().minGroups(intervals) == 3

    intervals = [[1, 3], [5, 6], [8, 10], [11, 13]]
    assert Solution().minGroups(intervals) == 1


if __name__ == '__main__':
    main()
