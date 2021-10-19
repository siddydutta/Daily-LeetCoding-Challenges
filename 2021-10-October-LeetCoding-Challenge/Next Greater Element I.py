# -*- coding: utf-8 -*-
from typing import List


class NotSolution:
    ''' Naive solution. Time Complexity: O(n^2). '''
    def nextGreaterElement(self, nums1: List[int],
                           nums2: List[int]) -> List[int]:
        result = list()
        for num in nums1:
            index = nums2.index(num)
            next_great = -1
            for next_num in nums2[index:]:
                if next_num > num:
                    next_great = next_num
                    break  # First greater element
            result.append(next_great)
        return result


class Solution:
    ''' Solution using monotonic stack. Time Complexity: O(n). '''
    def nextGreaterElement(self, nums1: List[int],
                           nums2: List[int]) -> List[int]:
        stack = list()  # Monotonically increasing stack
        next_index_map = dict()

        for num in nums2:
            while stack and stack[-1] < num:
                # Pop all numbers lesser than current number and map to current
                next_index_map[stack.pop()] = num
            stack.append(num)

        # Match answer for each element in nums1
        for index, num in enumerate(nums1):
            nums1[index] = next_index_map.get(num, -1)  # Get or default
        return nums1


def main():
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    assert Solution().nextGreaterElement(nums1, nums2) == [-1, 3, -1]

    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    assert Solution().nextGreaterElement(nums1, nums2) == [3, -1]


if __name__ == '__main__':
    main()
