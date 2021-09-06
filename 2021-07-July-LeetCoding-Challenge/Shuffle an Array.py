# -*- coding: utf-8 -*-
from random import shuffle
from typing import List


class Solution:
    ''' Simple pythonic solution. '''
    def __init__(self, nums: List[int]):
        self.array = nums
        self.array_copy = nums.copy()

    def reset(self) -> List[int]:
        ''' Resets the array to its original configuration and return it. '''
        return self.array

    def shuffle(self) -> List[int]:
        ''' Returns a random shuffling of the array. '''
        shuffle(self.array_copy)
        return self.array_copy


def main():
    nums = [1, 2, 3]
    obj = Solution(nums)
    assert set(obj.shuffle()) == set(nums)
    assert obj.reset() == nums
    assert set(obj.shuffle()) == set(nums)


if __name__ == '__main__':
    main()
