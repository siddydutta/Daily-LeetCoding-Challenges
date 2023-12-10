from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        return [[matrix[j][i] for j in range(rows)] for i in range(cols)]


def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert Solution().transpose(matrix) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    matrix = [[1, 2, 3], [4, 5, 6]]
    assert Solution().transpose(matrix) == [[1, 4], [2, 5], [3, 6]]


if __name__ == '__main__':
    main()
