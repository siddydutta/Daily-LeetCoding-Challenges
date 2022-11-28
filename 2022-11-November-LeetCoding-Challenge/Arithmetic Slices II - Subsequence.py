# -*- coding: utf-8 -*-
from collections import defaultdict
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        total = int()
        dp = [defaultdict(int) for _ in nums]
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    total += dp[j][diff]
        return total


def main():
    nums = [2, 4, 6, 8, 10]
    assert Solution().numberOfArithmeticSlices(nums) == 7

    nums = [7, 7, 7, 7, 7]
    assert Solution().numberOfArithmeticSlices(nums) == 16


if __name__ == '__main__':
    main()
