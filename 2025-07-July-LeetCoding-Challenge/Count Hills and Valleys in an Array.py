class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        count = 0
        for i in range(1, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i - 1]  # handle equal neighbours
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                count += 1  # hill count
            elif nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
                count += 1  # valley count
        return count


def main():
    nums = [2, 4, 1, 1, 6, 5]
    assert Solution().countHillValley(nums) == 3

    nums = [6, 6, 5, 5, 4, 1]
    assert Solution().countHillValley(nums) == 0


if __name__ == '__main__':
    main()
