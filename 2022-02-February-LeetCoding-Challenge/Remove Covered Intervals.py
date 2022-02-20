# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        ''' Brute force O(n^2) solution. '''
        n = len(intervals)
        for i in range(len(intervals)):
            a, b = intervals[i]
            for j in range(len(intervals)):
                c, d = intervals[j]
                # Compare every interval with others
                if i != j and c <= a and b <= d:
                    n -= 1
                    break  # Already removed, move to next
        return n


def main():
    intervals = [[1, 4], [3, 6], [2, 8]]
    assert Solution().removeCoveredIntervals(intervals) == 2

    intervals = [[1, 4], [2, 3]]
    assert Solution().removeCoveredIntervals(intervals) == 1


if __name__ == '__main__':
    main()
