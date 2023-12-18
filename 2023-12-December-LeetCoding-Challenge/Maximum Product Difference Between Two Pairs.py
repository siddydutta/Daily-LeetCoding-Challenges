from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1]*nums[-2]) - (nums[0]*nums[1])


def main():
    nums = [5, 6, 2, 7, 4]
    assert Solution().maxProductDifference(nums) == 34

    nums = [4, 2, 5, 9, 7, 4, 8]
    assert Solution().maxProductDifference(nums) == 64


if __name__ == '__main__':
    main()
