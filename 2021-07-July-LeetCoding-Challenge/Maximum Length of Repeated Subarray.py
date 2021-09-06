# -*- coding: utf-8 -*-
from typing import List


class Solution:
    '''
    Straight foward dynamic programming solution.
    Time Complexity: O(m*n)
    '''
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        ans = 0
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                if nums1[i] == nums2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                    ans = max(ans, dp[i+1][j+1])

        return ans


def main():
    obj = Solution()

    nums1 = [1, 2, 3, 2, 1]
    nums2 = [3, 2, 1, 4, 7]
    assert obj.findLength(nums1, nums2) == 3

    nums1 = [0, 0, 0, 0, 0]
    nums2 = [0, 0, 0, 0, 0]
    assert obj.findLength(nums1, nums2) == 5

    nums1 = [1, 2, 3, 2, 1]
    nums2 = [3, 2, 1, 4]
    assert obj.findLength(nums1, nums2) == 3


if __name__ == '__main__':
    main()
