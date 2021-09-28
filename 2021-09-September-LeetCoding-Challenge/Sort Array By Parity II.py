# -*- coding: utf-8 -*-
from typing import List


class Solution1:
    ''' In-place solution. '''
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        index = 0
        while index < len(nums):
            if index % 2 == 0 and nums[index] % 2 != 0:
                ptr = index + 1
                while nums[ptr] % 2 != 0:
                    ptr += 1
                nums[index], nums[ptr] = nums[ptr], nums[index]
            if index % 2 != 0 and nums[index] % 2 == 0:
                ptr = index + 1
                while nums[ptr] % 2 == 0:
                    ptr += 1
                nums[index], nums[ptr] = nums[ptr], nums[index]
            index += 1
        return nums


class Solution2:
    ''' Time optimized solution. '''
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ans = [None] * len(nums)
        even_ptr, odd_ptr = 0, 1

        for num in nums:
            if num % 2 == 0:
                ans[even_ptr] = num
                even_ptr += 2
            else:
                ans[odd_ptr] = num
                odd_ptr += 2

        return ans


class Solution:
    ''' In-place solution. '''
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even_ptr, odd_ptr = 0, 1
        n = len(nums)

        while even_ptr < n and odd_ptr < n:
            if nums[even_ptr] % 2 == 0:
                even_ptr += 2
            elif nums[odd_ptr] % 2 != 0:
                odd_ptr += 2
            else:
                nums[even_ptr], nums[odd_ptr] = nums[odd_ptr], nums[even_ptr]
                even_ptr += 2
                odd_ptr += 2

        return nums


def main():
    nums = [4, 2, 5, 7]
    assert Solution().sortArrayByParityII(nums) == [4, 5, 2, 7]

    nums = [2, 3]
    assert Solution().sortArrayByParityII(nums) == [2, 3]


if __name__ == '__main__':
    main()
