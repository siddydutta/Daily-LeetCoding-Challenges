from typing import List


class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        arr = [num for row in matrix for num in row]
        pos_arr = list(map(abs, arr))
        total, mi = sum(pos_arr), min(pos_arr)
        n_neg = sum([num < 0 for num in arr])
        return total if n_neg % 2 == 0 else total-2*mi


def main():
    matrix = [[1, -1],
              [-1, 1]]
    assert Solution().maxMatrixSum(matrix) == 4

    matrix = [[1, 2, 3],
              [-1, -2, -3],
              [1, 2, 3]]
    assert Solution().maxMatrixSum(matrix) == 16


if __name__ == '__main__':
    main()
