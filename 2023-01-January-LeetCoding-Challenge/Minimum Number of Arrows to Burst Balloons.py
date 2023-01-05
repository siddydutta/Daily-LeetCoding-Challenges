# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point: point[1])
        arrows, end = 1, points[0][1]
        for x_start, x_end in points[1:]:
            if x_start > end:
                arrows += 1
                end = x_end
        return arrows


def main():
    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
    assert Solution().findMinArrowShots(points) == 2

    points = [[1, 2], [3, 4], [5, 6], [7, 8]]
    assert Solution().findMinArrowShots(points) == 4

    points = [[1, 2], [2, 3], [3, 4], [4, 5]]
    assert Solution().findMinArrowShots(points) == 2


if __name__ == '__main__':
    main()
