# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        global_max = 0
        local_max = 0

        for bit in nums:
            if bit == 1:
                local_max += 1
            else:
                global_max = max(global_max, local_max)
                local_max = 0

        return max(global_max, local_max)


class DPSolution:
    ''' Dynamic programming solution. '''
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        max_count = 0 if nums[0] == 0 else 1
        dp = [0] * n
        dp[0] = 0 if nums[0] == 0 else 1

        for i in range(1, n):
            if nums[i] == 1:
                dp[i] = dp[i-1] + 1
                max_count = max(max_count, dp[i])
            else:
                dp[i] = 0

        return max_count


def main():
    nums = [1, 1, 0, 1, 1, 1]
    assert Solution().findMaxConsecutiveOnes(nums) == 3

    nums = [1, 0, 1, 1, 0, 1]
    assert Solution().findMaxConsecutiveOnes(nums) == 2


if __name__ == '__main__':
    main()
