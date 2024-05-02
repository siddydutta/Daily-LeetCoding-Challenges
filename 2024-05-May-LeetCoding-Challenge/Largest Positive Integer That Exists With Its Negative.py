from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums = set(nums)
        largest = -1
        for num in nums:
            if num > 0 and -num in nums:
                largest = max(largest, num)
        return largest


def main():
    nums = [-1, 2, -3, 3]
    assert Solution().findMaxK(nums) == 3

    nums = [-1, 10, 6, 7, -7, 1]
    assert Solution().findMaxK(nums) == 7

    nums = [-10, 8, 6, 7, -2, -3]
    assert Solution().findMaxK(nums) == -1


if __name__ == '__main__':
    main()
