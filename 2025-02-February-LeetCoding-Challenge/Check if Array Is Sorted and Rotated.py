from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        return sum(nums[i] < nums[i-1] for i in range(len(nums))) <= 1


def main():
    nums = [3, 4, 5, 1, 2]
    assert Solution().check(nums) is True

    nums = [2, 1, 3, 4]
    assert Solution().check(nums) is False

    nums = [1, 2, 3]
    assert Solution().check(nums) is True


if __name__ == '__main__':
    main()
