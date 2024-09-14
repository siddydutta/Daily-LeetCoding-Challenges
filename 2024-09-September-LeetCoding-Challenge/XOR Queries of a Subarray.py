from itertools import accumulate
from operator import xor
from typing import List


class Solution:
    def xorQueries(
            self, arr: List[int], queries: List[List[int]]
    ) -> List[int]:
        prefix_sums = list(accumulate(arr, xor))
        result = []
        for i, j in queries:
            if i == 0:
                result.append(prefix_sums[j])
            else:
                result.append(prefix_sums[i-1] ^ prefix_sums[j])
        return result


def main():
    arr = [1, 3, 4, 8]
    queries = [[0, 1], [1, 2], [0, 3], [3, 3]]
    assert Solution().xorQueries(arr, queries) == [2, 7, 14, 8]

    arr = [4, 8, 2, 10]
    queries = [[2, 3], [1, 3], [0, 0], [0, 3]]
    assert Solution().xorQueries(arr, queries) == [8, 0, 4, 4]


if __name__ == '__main__':
    main()
