from typing import List


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        res, n = 0, len(nums)
        for i in range(1, n):
            if nums[i-1] < nums[i]:
                res += (n - i)
        return res


def main():
    nums = [5, 1, 3]
    assert Solution().reductionOperations(nums) == 3

    nums = [1, 1, 1]
    assert Solution().reductionOperations(nums) == 0

    nums = [1, 1, 2, 2, 3]
    assert Solution().reductionOperations(nums) == 4


if __name__ == '__main__':
    main()
