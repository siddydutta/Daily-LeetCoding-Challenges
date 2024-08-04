from typing import List


class Solution:
    def rangeSum(self, nums: List[int], _: int, left: int, right: int) -> int:
        sums = []
        for i in range(len(nums)):
            s = 0
            for j in range(i, len(nums)):
                s += nums[j]
                sums.append(s)
        sums.sort()
        return sum(sums[left-1:right]) % (10**9 + 7)


def main():
    nums = [1, 2, 3, 4]
    n = 4
    left = 1
    right = 5
    assert Solution().rangeSum(nums, n, left, right) == 13

    nums = [1, 2, 3, 4]
    n = 4
    left = 3
    right = 4
    assert Solution().rangeSum(nums, n, left, right) == 6

    nums = [1, 2, 3, 4]
    n = 4
    left = 1
    right = 10
    assert Solution().rangeSum(nums, n, left, right) == 50


if __name__ == '__main__':
    main()
