# -*- coding: utf-8 -*-
from bisect import bisect_left, insort
from itertools import accumulate, product, combinations
from math import inf
from typing import List


class Solution:
    '''
    Time Complexity: O(m^2 * n^2)
    '''
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        M = len(matrix)  # Number of rows
        N = len(matrix[0])  # Number of columns
        ans = -inf

        def countRangeSum(nums, upper):
            '''
            Logic from 327. Count of Range Sum
            '''
            sorted_list = [0]
            ans = -inf
            for s in accumulate(nums):  # Prefix sums
                index = bisect_left(sorted_list, s - upper)
                if index < len(sorted_list):
                    ans = max(ans, s - sorted_list[index])
                insort(sorted_list, s)
            return ans

        # Calculate column wise prefix sums
        for i, j in product(range(1, M), range(N)):
            matrix[i][j] += matrix[i-1][j]  # this row = this row + prev row
        matrix = [[0]*N] + matrix  # Insert a zero row

        # Row wise, prepare differences and apply count range sum function
        for row1, row2 in combinations(range(M+1), 2):
            row = [j-i for i, j in zip(matrix[row1], matrix[row2])]
            ans = max(ans, countRangeSum(row, k))

        return ans


def main():
    obj = Solution()

    matrix = [[1, 0, 1], [0, -2, 3]]
    k = 2
    assert obj.maxSumSubmatrix(matrix, k) == 2

    matrix = [[2, 2, -1]]
    k = 3
    assert obj.maxSumSubmatrix(matrix, k) == 3


if __name__ == '__main__':
    main()
