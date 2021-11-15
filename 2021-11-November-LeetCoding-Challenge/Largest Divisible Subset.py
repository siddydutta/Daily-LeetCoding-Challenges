# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count, pre = [0] * n, [0] * n
        nums.sort()

        maxx, index = 0, -1
        for i in range(n):
            count[i] = 1
            pre[i] = -1
            for j in range(i-1, -1, -1):
                if nums[i] % nums[j] == 0:
                    if count[j]+1 > count[i]:
                        count[i] = count[j] + 1
                        pre[i] = j
            if count[i] > maxx:
                maxx = count[i]
                index = i

        res = list()
        while index != -1:
            res.append(nums[index])
            index = pre[index]
        return res


def main():
    nums = [1, 2, 3]
    assert Solution().largestDivisibleSubset(nums) == [2, 1]

    nums = [1, 2, 4, 8]
    assert Solution().largestDivisibleSubset(nums) == [8, 4, 2, 1]


if __name__ == '__main__':
    main()
