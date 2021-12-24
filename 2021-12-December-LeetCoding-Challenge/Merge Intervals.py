# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ''' Sorting based solution. '''
        intervals = sorted(intervals, key=lambda x: x[0])
        idx = int()
        while idx < len(intervals)-1:
            if intervals[idx][1] >= intervals[idx+1][0]:
                # Create merged interval
                merged = [intervals[idx][0],
                          max(intervals[idx][1], intervals[idx+1][1])]
                # Remove intervals
                intervals.pop(idx)
                intervals.pop(idx)
                # Insert merged interval
                intervals.insert(idx, merged)
            else:
                idx += 1  # Move on to next interval
        return intervals


def main():
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    assert Solution().merge(intervals) == [[1, 6], [8, 10], [15, 18]]

    intervals = [[1, 4], [4, 5]]
    assert Solution().merge(intervals) == [[1, 5]]

    intervals = [[1, 4], [2, 3]]
    assert Solution().merge(intervals) == [[1, 4]]


if __name__ == '__main__':
    main()
