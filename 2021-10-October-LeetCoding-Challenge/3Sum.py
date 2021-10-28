# -*- coding: utf-8 -*-
from typing import List


class Solution:
    ''' Time Complexity: O(n^2) '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return list()

        three_sums = set()
        for i in range(len(nums)-1):
            sum_set = set()
            for j in range(i+1, len(nums)):
                req = -(nums[i] + nums[j])
                if req in sum_set:
                    three_sum = tuple(sorted((nums[i], nums[j], req)))
                    three_sums.add(three_sum)
                else:
                    sum_set.add(nums[j])
        return list(map(list, three_sums))


def main():
    nums = [-1, 0, 1, 2, -1, -4]
    assert Solution().threeSum(nums) == [[-1, -1, 2], [-1, 0, 1]]

    nums = []
    assert Solution().threeSum(nums) == []


if __name__ == '__main__':
    main()
