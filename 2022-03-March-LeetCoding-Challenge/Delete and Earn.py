# -*- coding: utf-8 -*-
from collections import Counter
from typing import List


class Solution1:
    def deleteAndEarn(self, nums: List[int]) -> int:
        ''' Dynamic programming solution. '''
        buckets, dp = [0] * 10001, [0] * 10001
        for num in nums:
            buckets[num] += num

        dp[0], dp[1] = buckets[0], buckets[1]
        for i in range(2, len(buckets)):
            dp[i] = max(buckets[i]+dp[i-2], dp[i-1])

        return dp[10000]


class Solution2:
    def deleteAndEarn(self, nums: List[int]) -> int:
        ''' Pythonic DP solution. '''
        freq = Counter(nums)
        prev_max, curr_max = 0, 0
        for num in range(max(nums)+1):
            prev_max, curr_max = curr_max, max(curr_max, prev_max+freq[num]*num)
        return curr_max


def main():
    for obj in [Solution1(), Solution2()]:
        nums = [3, 4, 2]
        assert obj.deleteAndEarn(nums) == 6

        nums = [2, 2, 3, 3, 3, 4]
        assert obj.deleteAndEarn(nums) == 9


if __name__ == '__main__':
    main()
