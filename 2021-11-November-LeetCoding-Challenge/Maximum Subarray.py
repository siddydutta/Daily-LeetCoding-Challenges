# -*- coding: utf-8 -*-
from math import inf
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ''' Dynamic programming solution. '''
        dp = [-inf] * len(nums)
        dp[0] = nums[0]
        max_sum = dp[0]

        for i in range(1, len(nums)):
            # dp[i] is the max of including the current number in running sum
            # or start from scratch
            dp[i] = max(nums[i], dp[i-1]+nums[i])
            max_sum = max(max_sum, dp[i])

        return max_sum


def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert Solution().maxSubArray(nums) == 6

    nums = [1]
    assert Solution().maxSubArray(nums) == 1

    nums = [5, 4, -1, 7, 8]
    assert Solution().maxSubArray(nums) == 23


if __name__ == '__main__':
    main()
