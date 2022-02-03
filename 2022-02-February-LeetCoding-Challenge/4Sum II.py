# -*- coding: utf-8 -*-
from collections import defaultdict
from itertools import product
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int],
                     nums3: List[int], nums4: List[int]) -> int:
        ''' Solution based on two-sum, but works on pairs. '''
        pair_frequency = defaultdict(int)
        for x, y in product(nums1, nums2):
            pair_frequency[x+y] += 1

        count = 0
        for x, y in product(nums3, nums4):
            count += pair_frequency.get(-(x+y), 0)
        return count


def main():
    nums1 = [1, 2]
    nums2 = [-2, -1]
    nums3 = [-1, 2]
    nums4 = [0, 2]
    assert Solution().fourSumCount(nums1, nums2, nums3, nums4) == 2

    nums1 = [0]
    nums2 = [0]
    nums3 = [0]
    nums4 = [0]
    assert Solution().fourSumCount(nums1, nums2, nums3, nums4) == 1


if __name__ == '__main__':
    main()
