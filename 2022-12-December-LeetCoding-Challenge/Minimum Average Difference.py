# -*- coding: utf-8 -*-
from itertools import accumulate
from math import inf
from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        total_sum, n = sum(nums), len(nums)
        prefix_nums = list(accumulate(nums))
        min_avg_diff, min_avg_diff_idx = inf, 0

        for i in range(n):
            lhs = prefix_nums[i] // (i+1)
            rhs = (total_sum - prefix_nums[i]) // (n-i-1) if i != n-1 else 0
            avg_diff = abs(lhs - rhs)
            if avg_diff < min_avg_diff:
                min_avg_diff = avg_diff
                min_avg_diff_idx = i

        return min_avg_diff_idx


def main():
    nums = [2, 5, 3, 9, 5, 3]
    assert Solution().minimumAverageDifference(nums) == 3

    nums = [0]
    assert Solution().minimumAverageDifference(nums) == 0


if __name__ == '__main__':
    main()
