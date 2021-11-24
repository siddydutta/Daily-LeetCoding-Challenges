# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]],
                             secondList: List[List[int]]) -> List[List[int]]:
        ''' Solution based on two-pointer approach. '''
        ptr1, ptr2 = 0, 0
        m, n = len(firstList), len(secondList)
        intervals = list()
        while ptr1 < m and ptr2 < n:
            # Try to find common intersection
            start = max(firstList[ptr1][0], secondList[ptr2][0])
            end = min(firstList[ptr1][1], secondList[ptr2][1])
            if start <= end:
                # Valid intersection
                intervals.append([start, end])

            # Move pointer of list having the smaller end time
            if firstList[ptr1][1] < secondList[ptr2][1]:
                ptr1 += 1
            else:
                ptr2 += 1
        return intervals


def main():
    firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
    secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
    intervals = [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
    assert Solution().intervalIntersection(firstList, secondList) == intervals

    firstList = [[1, 3], [5, 9]]
    secondList = []
    assert Solution().intervalIntersection(firstList, secondList) == []

    firstList = []
    secondList = [[4, 8], [10, 12]]
    assert Solution().intervalIntersection(firstList, secondList) == []

    firstList = [[1, 7]]
    secondList = [[3, 10]]
    assert Solution().intervalIntersection(firstList, secondList) == [[3, 7]]


if __name__ == '__main__':
    main()
