from itertools import product


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> list[list[int]]:
        rows, cols = len(matrix), len(matrix[0])
        first_row_zero, first_col_zero = False, False

        for row, col in product(range(rows), range(cols)):
            if matrix[row][col] == 0:
                if row == 0:
                    first_row_zero = True
                if col == 0:
                    first_col_zero = True
                matrix[row][0] = None
                matrix[0][col] = None

        for row in range(1, rows):
            if matrix[row][0] is None:
                for col in range(cols):
                    matrix[row][col] = 0
        for col in range(1, cols):
            if matrix[0][col] is None:
                for row in range(rows):
                    matrix[row][col] = 0

        if first_col_zero is True:
            for row in range(rows):
                matrix[row][0] = 0
        if first_row_zero is True:
            for col in range(cols):
                matrix[0][col] = 0


def main():
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    Solution().setZeroes(matrix)
    assert matrix == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    matrix = [[0, 1, 2, 0],
              [3, 4, 5, 2],
              [1, 3, 1, 5]]
    Solution().setZeroes(matrix)
    assert matrix == [[0, 0, 0, 0],
                      [0, 4, 5, 0],
                      [0, 3, 1, 0]]

    matrix = [[1, 2, 3, 4],
              [5, 0, 7, 8],
              [0, 10, 11, 12],
              [13, 14, 15, 0]]
    Solution().setZeroes(matrix)
    assert matrix == [[0, 0, 3, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]


if __name__ == '__main__':
    main()
