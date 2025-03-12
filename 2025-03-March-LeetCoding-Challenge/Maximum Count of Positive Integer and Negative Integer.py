class Solution:
    def __binary_search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        position = len(nums)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                position = mid
                right = mid - 1
        return position

    def maximumCount(self, nums: list[int]) -> int:
        negatives = self.__binary_search(nums, 0)
        positives = len(nums) - self.__binary_search(nums, 1)
        return max(negatives, positives)


def main():
    nums = [-2, -1, -1, 1, 2, 3]
    assert Solution().maximumCount(nums) == 3

    nums = [-3, -2, -1, 0, 0, 1, 2]
    assert Solution().maximumCount(nums) == 3

    nums = [5, 20, 66, 1314]
    assert Solution().maximumCount(nums) == 4


if __name__ == '__main__':
    main()
