class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        or_sum = 0
        for num in nums:
            or_sum |= num
        return or_sum * (1 << (len(nums) - 1))


def main():
    nums = [1, 3]
    assert Solution().subsetXORSum(nums) == 6

    nums = [5, 1, 6]
    assert Solution().subsetXORSum(nums) == 28

    nums = [3, 4, 5, 6, 7, 8]
    assert Solution().subsetXORSum(nums) == 480


if __name__ == '__main__':
    main()
