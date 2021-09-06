# -*- coding: utf-8 -*-
from typing import List


class NaiveSolution:
    '''
    The sum of the length of any two sides of a triangle must be greater than
    the length of the third side.
    Brute force approach.
    Time Complexity: O(n^3)
    '''
    def triangleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] > nums[k] and \
                        nums[j] + nums[k] > nums[i] and \
                            nums[k] + nums[i] > nums[j]:
                        ans += 1
        return ans


class Solution:
    '''
    Solution based on sorting and two pointers approach.
    Time Complexity: O(n^2)
    '''
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0

        # For every number, check if there are two numbers whose sum is greater
        for i in range(2, len(nums)):
            left = 0
            right = i-1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    ans += (right - left)  # All numbers in range fit criteria
                    right -= 1
                else:
                    left += 1

        return ans


def main():
    obj = Solution()

    nums = [2, 2, 3, 4]
    assert obj.triangleNumber(nums) == 3

    nums = [4, 2, 3, 4]
    assert obj.triangleNumber(nums) == 4

    nums = [0, 1, 0]
    assert obj.triangleNumber(nums) == 0


if __name__ == '__main__':
    main()
