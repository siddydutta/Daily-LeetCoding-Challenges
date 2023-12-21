from itertools import pairwise
from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        max_diff = float('-inf')
        points.sort()
        for (x1, _), (x2, _) in pairwise(sorted(points)):
            max_diff = max(max_diff, x2 - x1)
        return max_diff
        # return max(x2 - x1 for x1, x2 in pairwise(sorted(x for x, _ in points)))


def main():
    points = [[8, 7], [9, 9], [7, 4], [9, 7]]
    assert Solution().maxWidthOfVerticalArea(points) == 1

    points = [[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]
    assert Solution().maxWidthOfVerticalArea(points) == 3


if __name__ == '__main__':
    main()
