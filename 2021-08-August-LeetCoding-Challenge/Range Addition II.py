# -*- coding: utf-8 -*-
from typing import List


class Solution:
    '''
    Straightforward solution.
    The maximum integer is always at position [0, 0] as it is incremented with
    every operation.
    The count of maximum integers then becomes the minimum position in the
    operations list.
    Time Complexity: O(len(ops))
    '''
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        for x, y in ops:
            m = min(m, x)
            n = min(n, y)
        return m * n  # All integers in m by n grid are maximum incremented.


def main():
    m, n = 3, 3
    ops = [[2, 2], [3, 3]]
    assert Solution().maxCount(m, n, ops) == 4

    m, n = 3, 3
    ops = [[2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3],
           [2, 2], [3, 3], [3, 3], [3, 3]]
    assert Solution().maxCount(m, n, ops) == 4

    m, n = 3, 3
    ops = []
    assert Solution().maxCount(m, n, ops) == 9


if __name__ == '__main__':
    main()
