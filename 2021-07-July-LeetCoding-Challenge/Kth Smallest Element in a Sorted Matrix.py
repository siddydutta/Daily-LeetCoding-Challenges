# -*- coding: utf-8 -*-
from bisect import bisect
from typing import List


class Solution1:
    '''
    Trivial solution.
    '''
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # Flatten List
        elements = [element for row in matrix for element in row]
        elements.sort()
        return elements[k-1]  # k is a 1 based index


class Solution:
    '''
    Using binary search.
    '''
    def count(self, matrix: List[List[int]], num: int) -> int:
        '''
        Returns the number of values less than or equal to num (mid value),
        using binary search over each row.
        '''
        count = 0
        for row in matrix:
            count += bisect(row, num)
        return count

    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        left = matrix[0][0]  # First element is the smallest
        right = matrix[-1][-1]  # Last element is the greatest

        while left <= right:
            mid = (left + right) // 2
            if self.count(matrix, mid) < k:
                left = mid + 1
            else:
                right = mid - 1

        return left


def main():
    obj = Solution()

    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    assert obj.kthSmallest(matrix, k) == 13

    matrix = [[-5]]
    k = 1
    assert obj.kthSmallest(matrix, k) == -5

    matrix = [[1, 2], [1, 3]]
    k = 3
    assert obj.kthSmallest(matrix, k) == 2


if __name__ == '__main__':
    main()
