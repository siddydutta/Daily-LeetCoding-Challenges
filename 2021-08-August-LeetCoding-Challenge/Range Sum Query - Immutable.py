# -*- coding: utf-8 -*-
from itertools import accumulate
from typing import List


class NaiveNumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:right+1])


class NumArray:
    ''' Solution based on prefix sums. '''
    def __init__(self, nums: List[int]):
        self.sums = list(accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sums[right]
        return self.sums[right] - self.sums[left - 1]


def main():
    numArray = NumArray([-2, 0, 3, -5, 2, -1])
    assert numArray.sumRange(0, 2) == 1
    assert numArray.sumRange(2, 5) == -1
    assert numArray.sumRange(0, 5) == -3


if __name__ == '__main__':
    main()
