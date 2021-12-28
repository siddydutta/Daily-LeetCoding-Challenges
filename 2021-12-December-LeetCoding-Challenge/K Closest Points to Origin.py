# -*- coding: utf-8 -*-
from heapq import nsmallest
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ''' Solution using Python's heapq library. '''
        return nsmallest(k, points, lambda x: x[0] ** 2 + x[1] ** 2)


def main():
    points = [[1, 3], [-2, 2]]
    k = 1
    assert Solution().kClosest(points, k) == [[-2, 2]]

    points = [[3, 3], [5, -1], [-2, 4]]
    k = 2
    assert Solution().kClosest(points, k) == [[3, 3], [-2, 4]]


if __name__ == '__main__':
    main()
