# -*- coding: utf-8 -*-
from typing import List


class NaiveSolution:
    '''
    Brute force solution.
    Time Complexity: O(n^2)
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return  # Dummy return


class Solution:
    '''
    Two pass solution using a hashmap for number indices.
    Time Complexity: O(n)
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndexMap = dict()  # Number -> Index

        for index, num in enumerate(nums):
            numIndexMap[num] = index  # Stores the latest index of a number

        for index1, num in enumerate(nums):
            difference = target - num  # Difference is the required number
            if difference in numIndexMap:
                index2 = numIndexMap.get(difference)
                if index1 != index2:
                    # The same number cannot be used twice
                    return [index1, index2]
        return  # Dummy return


def main():
    nums = [2, 7, 11, 15]
    target = 9
    assert Solution().twoSum(nums, target) == [0, 1]

    nums = [3, 2, 4]
    target = 6
    assert Solution().twoSum(nums, target) == [1, 2]

    nums = [3, 3]
    target = 6
    assert Solution().twoSum(nums, target) == [0, 1]


if __name__ == '__main__':
    main()
