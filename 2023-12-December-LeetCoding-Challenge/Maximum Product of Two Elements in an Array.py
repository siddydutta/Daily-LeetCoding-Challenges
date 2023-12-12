from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-2]-1) * (nums[-1]-1)


def main():
    nums = [3, 4, 5, 2]
    assert Solution().maxProduct(nums) == 12

    nums = [1, 5, 4, 5]
    assert Solution().maxProduct(nums) == 16

    nums = [3, 7]
    assert Solution().maxProduct(nums) == 12


if __name__ == '__main__':
    main()
