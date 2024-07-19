from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        mins = {min(row) for row in matrix}
        maxs = {max(col) for col in zip(*matrix)}
        return list(mins.intersection(maxs))


def main():
    matrix = [[3, 7, 8],
              [9, 11, 13],
              [15, 16, 17]]
    assert Solution().luckyNumbers(matrix) == [15]

    matrix = [[1, 10, 4, 2],
              [9, 3, 8, 7],
              [15, 16, 17, 12]]
    assert Solution().luckyNumbers(matrix) == [12]

    matrix = [[7, 8],
              [1, 2]]
    assert Solution().luckyNumbers(matrix) == [7]


if __name__ == '__main__':
    main()
