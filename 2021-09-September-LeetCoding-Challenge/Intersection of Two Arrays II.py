# -*- coding: utf-8 -*-
from collections import defaultdict
from typing import List


class Solution1:
    ''' Straightforward solution. '''
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_map = defaultdict(int)
        num2_map = defaultdict(int)
        for num in nums1:
            num1_map[num] += 1
        for num in nums2:
            num2_map[num] += 1

        intersection = list()
        for key in num1_map.keys():
            if key in num2_map:
                common = min(num1_map.get(key), num2_map.get(key))
                intersection += [key] * common

        return intersection


class Solution:
    ''' Solution based on sorting. '''
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        intersection = list()

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                intersection.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return intersection


def main():
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    assert Solution().intersect(nums1, nums2) == [2, 2]

    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    assert Solution().intersect(nums1, nums2) == [4, 9] or \
        Solution().intersect(nums1, nums2) == [9, 4]


if __name__ == '__main__':
    main()
