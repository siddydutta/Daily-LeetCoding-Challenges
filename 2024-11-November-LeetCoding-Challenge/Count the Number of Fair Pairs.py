from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def count_lower(val: int) -> int:
            res, j = 0, len(nums)-1
            for i in range(len(nums)):
                while i < j and nums[i] + nums[j] > val:
                    j -= 1
                res += max(0, j-i)
            return res
        nums.sort()
        return count_lower(upper) - count_lower(lower-1)


def main():
    nums = [0, 1, 7, 4, 4, 5]
    lower = 3
    upper = 6
    assert Solution().countFairPairs(nums, lower, upper) == 6

    nums = [1, 7, 9, 2, 5]
    lower = 11
    upper = 11
    assert Solution().countFairPairs(nums, lower, upper) == 1


if __name__ == '__main__':
    main()
