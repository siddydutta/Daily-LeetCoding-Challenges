# -*- coding: utf-8 -*-
from math import inf
from typing import List


class NaiveSolution:
    '''
    Naive solution
    Time Complexiy: O(n)
    '''
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.insert(0, -inf)
        nums.append(-inf)

        for i in range(1, n+1):
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i-1  # Since extra elements were added

        return 0  # Dummy return


class Solution:
    '''
    Using binary search
    Time Complexity: O(log n)
    '''
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        # Base case for single element
        if n == 1:
            return 0
        # Boundary elements case
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return n-1

        left = 0
        right = n-1

        while left <= right:
            mid = left + (right - left) // 2
            # Check if mid element is a peak element
            if (mid == 0 or nums[mid] > nums[mid-1]) \
                    and (mid == n-1 or nums[mid] > nums[mid+1]):
                return mid
            # If left element is greater, then check left half
            elif (mid > 0 and nums[mid-1] > nums[mid]):
                right = mid - 1
            # Otherwise check right half
            else:
                left = mid + 1


class RecursiveSolution:
    def findPeakElement(self, nums: List[int]) -> int:
        def binarySearch(left: int, right: int) -> int:
            if left == right:
                return left
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid+1]:
                return binarySearch(mid+1, right)
            else:
                return binarySearch(left, mid)
        return binarySearch(0, len(nums)-1)


def main():
    solutions = [NaiveSolution(), Solution(), RecursiveSolution()]

    for obj in solutions:
        nums = [0]
        assert obj.findPeakElement(nums) == 0

        nums = [1, 2, 3, 1]
        assert obj.findPeakElement(nums) == 2

        nums = [2, 1]
        assert obj.findPeakElement(nums) == 0

        nums = [1, 2, 1, 3, 5, 6, 4]
        assert obj.findPeakElement(nums) in [1, 5]

        nums = [1, 2, 3, 4, 5]
        assert obj.findPeakElement(nums) == 4

        nums = [3, 4, 3, 2, 1]
        assert obj.findPeakElement(nums) == 1


if __name__ == '__main__':
    main()
