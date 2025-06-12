class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        return max(abs(n1 - n2) for n1, n2 in zip(nums, nums[1:] + nums[:1]))


def main():
    nums = [1, 2, 4]
    assert Solution().maxAdjacentDistance(nums) == 3

    nums = [-5, -10, -5]
    assert Solution().maxAdjacentDistance(nums) == 5


if __name__ == '__main__':
    main()
