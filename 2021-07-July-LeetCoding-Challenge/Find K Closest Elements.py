# -*- coding: utf-8 -*-
from typing import List
from bisect import bisect_left


class NonOptimalSolution:
    '''
    First apply binary search on the given sorted array to find where
    element x would be inserted.
    The elements around x's insertion position are the closest elements.
    Use a two-pointer approach to add k closest elements.
    Time Complexity: O(n)
    '''
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if len(arr) == k:
            return arr

        left_ptr = bisect_left(arr, x) - 1
        right_ptr = left_ptr + 1

        elements = list()
        while len(elements) != k:
            if left_ptr >= 0 and right_ptr < len(arr):
                # Left element is closer than right element
                if abs(arr[left_ptr] - x) <= abs(arr[right_ptr] - x):
                    elements.insert(0, arr[left_ptr])
                    left_ptr -= 1
                else:
                    elements.append(arr[right_ptr])
                    right_ptr += 1
            # No more elements on the left side
            elif left_ptr < 0:
                elements.append(arr[right_ptr])
                right_ptr += 1
            # No more elements on the right side
            elif right_ptr >= len(arr):
                elements.insert(0, arr[left_ptr])
                left_ptr -= 1

        return elements


class Solution:
    '''
    The k closest elements range can be found while applying binary search.
    Time Complexity: O(logn)
    '''
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k

        while left < right:
            mid = (left + right) // 2
            # According to given conditions
            if x - arr[mid] <= arr[mid+k] - x:
                right = mid
            else:
                left = mid + 1

        return arr[left:left+k]


def main():
    obj = Solution()

    arr = [1, 2, 3, 4, 5]
    k = 4
    x = 3
    assert obj.findClosestElements(arr, k, x) == [1, 2, 3, 4]
    x = -1
    assert obj.findClosestElements(arr, k, x) == [1, 2, 3, 4]

    arr = [0, 0, 1, 2, 3, 3, 4, 7, 7, 8]
    k = 3
    x = 5
    assert obj.findClosestElements(arr, k, x) == [3, 3, 4]


if __name__ == '__main__':
    main()
