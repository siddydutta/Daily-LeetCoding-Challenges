# -*- coding: utf-8 -*-
from math import inf
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        '''
        Solution based on sorting and two pass approach.
        Time Complexity: O(nlogn) + O(n)    Space Complexity: O(1)
        '''
        arr.sort()
        min_abs_diff = inf
        # Pass 1: Find minimum absolute difference
        for i in range(1, len(arr)):
            min_abs_diff = min(min_abs_diff, arr[i]-arr[i-1])
        # Pass 2: Get pairs that have the minimum absolute difference
        ans = list()
        for i in range(1, len(arr)):
            if arr[i]-arr[i-1] == min_abs_diff:
                ans.append([arr[i-1], arr[i]])
        return ans


def main():
    arr = [4, 2, 1, 3]
    assert Solution().minimumAbsDifference(arr) == [[1, 2], [2, 3], [3, 4]]

    arr = [1, 3, 6, 10, 15]
    assert Solution().minimumAbsDifference(arr) == [[1, 3]]

    arr = [3, 8, -10, 23, 19, -4, -14, 27]
    assert Solution().minimumAbsDifference(arr) == [[-14, -10], [19, 23], [23, 27]]


if __name__ == '__main__':
    main()
