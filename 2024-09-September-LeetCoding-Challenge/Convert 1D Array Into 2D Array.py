from itertools import product
from typing import List


class Solution:
    def construct2DArray(
            self, original: List[int], m: int, n: int
    ) -> List[List[int]]:
        if m*n != len(original):
            return []
        array = [[None]*n for _ in range(m)]
        idx = 0
        for i, j in product(range(m), range(n)):
            array[i][j] = original[idx]
            idx += 1
        return array


def main():
    original = [1, 2, 3, 4]
    m = 2
    n = 2
    assert Solution().construct2DArray(original, m, n) == [[1, 2],
                                                           [3, 4]]

    original = [1, 2, 3]
    m = 1
    n = 3
    assert Solution().construct2DArray(original, m, n) == [[1, 2, 3]]

    original = [1, 2]
    m = 1
    n = 1
    assert Solution().construct2DArray(original, m, n) == []


if __name__ == '__main__':
    main()
