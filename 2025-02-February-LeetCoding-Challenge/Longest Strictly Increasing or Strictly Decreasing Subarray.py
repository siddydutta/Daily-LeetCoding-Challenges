from itertools import pairwise
from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        curr_incr, curr_decr = 1, 1
        max_len = 1
        for n1, n2 in pairwise(nums):
            curr_incr = (n1 < n2) * curr_incr + 1
            curr_decr = (n1 > n2) * curr_decr + 1
            max_len = max(max_len, curr_incr, curr_decr)
        return max_len


def main():
    nums = [1, 4, 3, 3, 2]
    assert Solution().longestMonotonicSubarray(nums) == 2

    nums = [3, 3, 3, 3]
    assert Solution().longestMonotonicSubarray(nums) == 1

    nums = [3, 2, 1]
    assert Solution().longestMonotonicSubarray(nums) == 3


if __name__ == '__main__':
    main()
