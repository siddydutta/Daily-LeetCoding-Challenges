# -*- coding: utf-8 -*-
from collections import defaultdict
from typing import List


class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        rank = [0] * (rows + cols)

        # Map store values to indices for easy access
        indices = defaultdict(list)  # Value -> [Row, Col] position
        for row in range(rows):
            for col in range(cols):
                indices[matrix[row][col]].append([row, col])

        # Find algorithm for DSU
        def find(index):
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]

        for val in sorted(indices):
            parent = list(range(rows + cols))
            rank2 = rank.copy()
            for row, col in indices[val]:
                row, col = find(row), find(rows + col)
                parent[row] = col
                rank2[col] = max(rank2[row], rank2[col])
            for row, col in indices[val]:
                rank[row] = rank[rows + col] = \
                    matrix[row][col] = rank2[find(row)] + 1

        return matrix


def main():
    matrix = [[1, 2],
              [3, 4]]
    assert Solution().matrixRankTransform(matrix) == [[1, 2],
                                                      [2, 3]]

    matrix = [[7, 7],
              [7, 7]]
    assert Solution().matrixRankTransform(matrix) == [[1, 1],
                                                      [1, 1]]

    matrix = [[20, -21, 14],
              [-19, 4, 19],
              [22, -47, 24],
              [-19, 4, 19]]
    assert Solution().matrixRankTransform(matrix) == [[4, 2, 3],
                                                      [1, 3, 4],
                                                      [5, 1, 6],
                                                      [1, 3, 4]]

    matrix = [[7, 3, 6],
              [1, 4, 5],
              [9, 8, 2]]
    assert Solution().matrixRankTransform(matrix) == [[5, 1, 4],
                                                      [1, 2, 3],
                                                      [6, 3, 1]]


if __name__ == '__main__':
    main()
