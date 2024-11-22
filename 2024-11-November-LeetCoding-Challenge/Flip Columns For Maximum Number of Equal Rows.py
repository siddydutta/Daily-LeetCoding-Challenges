from collections import defaultdict
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern_counts = defaultdict(int)
        for row in matrix:
            pattern = tuple(row)
            complement = tuple(1 - x for x in row)
            canonical = min(pattern, complement)
            pattern_counts[canonical] += 1
        return max(pattern_counts.values())


def main():
    matrix = [[0, 1],
              [1, 1]]
    assert Solution().maxEqualRowsAfterFlips(matrix) == 1

    matrix = [[0, 1],
              [1, 0]]
    assert Solution().maxEqualRowsAfterFlips(matrix) == 2

    matrix = [[0, 0, 0],
              [0, 0, 1],
              [1, 1, 0]]
    assert Solution().maxEqualRowsAfterFlips(matrix) == 2


if __name__ == '__main__':
    main()
