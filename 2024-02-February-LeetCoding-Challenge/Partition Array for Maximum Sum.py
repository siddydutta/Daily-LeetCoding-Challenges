from functools import lru_cache
from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        @lru_cache(None)
        def max_sum(idx: int) -> int:
            if idx >= len(arr):
                return 0
            length, max_val, curr_max = 0, 0, 0
            for j in range(idx, idx+k):
                if j >= len(arr):
                    break
                length += 1
                max_val = max(max_val, arr[j])  # max in current sub array
                curr_max = max(curr_max, max_val*length + max_sum(j+1))
            return curr_max
        return max_sum(0)


def main():
    arr = [1, 15, 7, 9, 2, 5, 10]
    k = 3
    assert Solution().maxSumAfterPartitioning(arr, k) == 84

    arr = [1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3]
    k = 4
    assert Solution().maxSumAfterPartitioning(arr, k) == 83

    arr = [1]
    k = 1
    assert Solution().maxSumAfterPartitioning(arr, k) == 1


if __name__ == '__main__':
    main()
