# -*- coding: utf-8 -*-
from bisect import bisect_left
from typing import List


class DPSolution:
    '''
    Dynamic programming solution.
    Bottom-up tabulation.
    Time Complexity: O(n^2)
    '''
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        max_length = 1
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j]+1:
                    dp[i] = dp[j] + 1
                    max_length = max(max_length, dp[i])

        return max_length


class Solution:
    '''
    Binary search based solution.
    Time Complexity: O(n*logn)
    '''
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = list()  # Longest increasing subsequence

        for num in nums:
            index = bisect_left(sub, num)  # Find insert position for num
            if index == len(sub):
                sub.append(num)  # Append a greater number
            else:
                sub[index] = num  # Replace with smaller number

        return len(sub)


def main():
    obj = Solution()

    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    assert obj.lengthOfLIS(nums) == 4

    nums = [0, 1, 0, 3, 2, 3]
    assert obj.lengthOfLIS(nums) == 4

    nums = [7, 7, 7, 7, 7, 7, 7]
    assert obj.lengthOfLIS(nums) == 1


if __name__ == '__main__':
    main()
