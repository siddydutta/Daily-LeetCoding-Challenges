class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        return [nums[nums[i]] for i in range(len(nums))]


def main():
    nums = [0, 2, 1, 5, 3, 4]
    assert Solution().buildArray(nums) == [0, 1, 2, 4, 5, 3]

    nums = [5, 0, 1, 2, 3, 4]
    assert Solution().buildArray(nums) == [4, 5, 0, 1, 2, 3]


if __name__ == '__main__':
    main()
