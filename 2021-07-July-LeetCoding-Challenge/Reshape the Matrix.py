# -*- coding: utf-8 -*-
from typing import List


class Solution1:
    '''
    Time Complexity: O(mn)
    '''
    def matrixReshape(self, mat: List[List[int]],
                      r: int, c: int) -> List[List[int]]:
        m = len(mat)  # Number of rows
        n = len(mat[0])  # Number of cols

        # Check if reshape with given parameters is possible
        if m*n != r*c:
            return mat

        row, col = 0, 0
        new_matrix = [[None] * c for _ in range(r)]

        # Simple mapping
        for i in range(m):
            for j in range(n):
                new_matrix[row][col] = mat[i][j]
                col += 1
                if col == c:
                    # Move to next row of new matrix
                    row += 1
                    col = 0

        return new_matrix


class Solution:
    '''
    Simple solution
    '''
    def matrixReshape(self, mat: List[List[int]],
                      r: int, c: int) -> List[List[int]]:
        m = len(mat)  # Number of rows
        n = len(mat[0])  # Number of cols

        # Check if reshape with given parameters is possible
        if m*n != r*c:
            return mat

        elements = [element for row in mat for element in row]  # Flatten mat
        new_matrix = list()

        for row in range(r):
            new_matrix.append(elements[row*c : (row+1)*c])

        return new_matrix


def main():
    obj = Solution()

    mat = [[1, 2], [3, 4]]
    r = 1
    c = 4
    assert obj.matrixReshape(mat, r, c) == [[1, 2, 3, 4]]

    r = 2
    assert obj.matrixReshape(mat, r, c) == [[1, 2], [3, 4]]

    mat = [[1, 2, 3], [4, 5, 6]]
    r = 3
    c = 2
    assert obj.matrixReshape(mat, r, c) == [[1, 2], [3, 4], [5, 6]]


if __name__ == '__main__':
    main()
