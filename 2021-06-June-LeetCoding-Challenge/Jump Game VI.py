# -*- coding: utf-8 -*-
from typing import List
from math import inf
from collections import deque


class Solution1:
    '''
    Using problem definition, a brute force solution using recursion.
    Time Complexity: O(k^n)
    '''
    def maxResult(self, nums: List[int], k: int, i: int = 0) -> int:
        if i >= len(nums) - 1:
            return nums[-1]  # Last element
        max_score = -inf
        for j in range(1, k+1):
            max_score = max(max_score, nums[i] + self.maxResult(nums, k, i+j))
        return max_score


class Solution2:
    '''
    Using dynamic programming, bottom-up approach (tabulation).
    dp[i] is the maximum score form index 0.
    Time Complexity: O(k*n)
    '''
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [-inf] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            for j in range(1, k+1):
                if i-j < 0:
                    continue
                dp[i] = max(dp[i], nums[i] + dp[i-j])
        return dp[-1]


class Solution3:
    '''
    Using dynamic programming, top-down approach (memoization).
    dp[i] is the the maximum score to reach the end starting at index i.
    Time Complextiy: O(k*n)
    '''
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [-inf] * len(nums)
        dp[-1] = nums[-1]

        def solve(nums: List[int], dp: List[int], i: int, k: int) -> int:
            if dp[i] != -inf:
                return dp[i]
            for j in range(1, k+1):
                if i+j < len(nums):
                    dp[i] = max(dp[i], nums[i] + solve(nums, dp, i+j, k))
            return dp[i]

        return solve(nums, dp, 0, k)


class Solution:
    '''
    Time Complexity: O(n)
    '''
    def maxResult(self, nums: List[int], k: int) -> int:
        dq = deque([0])  # Maintain indices, not numbers themselves

        for i in range(1, len(nums)):
            while dq and dq[0] < i-k:
                dq.popleft()  # Remove elements outside the k element window
            nums[i] += nums[dq[0]]  # First element of deque is max index
            while dq and nums[i] >= nums[dq[-1]]:
                dq.pop()  # To make space for new element and maintain order
            dq.append(i)

        return nums[-1]


if __name__ == '__main__':
    objects = [Solution(), Solution1(), Solution2(), Solution3()]
    for obj in objects:
        nums = [1, -1, -2, 4, -7, 3]
        k = 2
        assert obj.maxResult(nums, k) == 7

        nums = [10, -5, -2, 4, 0, 3]
        k = 3
        assert obj.maxResult(nums, k) == 17

        nums = [1, -5, -20, 4, -1, 3, -6, -3]
        k = 2
        assert obj.maxResult(nums, k) == 0
