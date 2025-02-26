class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        max_sum, min_sum = 0, 0
        ans = 0
        for num in nums:
            max_sum = max(max_sum + num, 0)
            min_sum = min(min_sum + num, 0)
            ans = max(ans, max_sum, -min_sum)
        return ans


def main():
    nums = [1, -3, 2, 3, -4]
    assert Solution().maxAbsoluteSum(nums) == 5

    nums = [2, -5, 1, -4, 3, -2]
    assert Solution().maxAbsoluteSum(nums) == 8


if __name__ == '__main__':
    main()
