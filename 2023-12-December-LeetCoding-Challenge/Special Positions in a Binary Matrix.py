from collections import defaultdict
from itertools import product
from typing import List


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row1s, col1s = defaultdict(int), defaultdict(int)
        m, n = len(mat), len(mat[0])
        for i, j in product(range(m), range(n)):
            row1s[i] += mat[i][j]
            col1s[j] += mat[i][j]
        count = 0
        for i, j in product(range(m), range(n)):
            if mat[i][j] == 1 and row1s[i] == 1 and col1s[j] == 1:
                count += 1
        return count


def main():
    mat = [[1, 0, 0],
           [0, 0, 1],
           [1, 0, 0]]
    assert Solution().numSpecial(mat) == 1

    mat = [[1, 0, 0],
           [0, 1, 0],
           [0, 0, 1]]
    assert Solution().numSpecial(mat) == 3


if __name__ == '__main__':
    main()
