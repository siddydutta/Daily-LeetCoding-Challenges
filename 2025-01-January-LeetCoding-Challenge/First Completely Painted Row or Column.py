from itertools import product
from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        row_count, col_count = [0] * rows, [0] * cols
        row_map, col_map = [0] * (rows*cols+1), [0] * (rows*cols+1)

        for row, col in product(range(rows), range(cols)):
            row_map[mat[row][col]] = row
            col_map[mat[row][col]] = col

        for idx, num in enumerate(arr):
            row_count[row_map[num]] += 1
            if row_count[row_map[num]] == cols:
                return idx
            col_count[col_map[num]] += 1
            if col_count[col_map[num]] == rows:
                return idx


def main():
    arr = [1, 3, 4, 2]
    mat = [[1, 4],
           [2, 3]]
    assert Solution().firstCompleteIndex(arr, mat) == 2

    arr = [2, 8, 7, 4, 1, 3, 5, 6, 9]
    mat = [[3, 2, 5],
           [1, 4, 6],
           [8, 7, 9]]
    assert Solution().firstCompleteIndex(arr, mat) == 3


if __name__ == '__main__':
    main()
