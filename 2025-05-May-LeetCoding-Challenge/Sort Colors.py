class Solution:
    def sortColors(self, nums: list[int]) -> None:
        left, right = 0, len(nums) - 1
        ptr = 0
        while ptr <= right:
            if nums[ptr] == 0:
                nums[left], nums[ptr] = nums[ptr], nums[left]
                left += 1
                ptr += 1
            elif nums[ptr] == 1:
                ptr += 1
            elif nums[ptr] == 2:
                nums[right], nums[ptr] = nums[ptr], nums[right]
                right -= 1


def main():
    nums = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]

    nums = [2, 0, 1]
    Solution().sortColors(nums)
    assert nums == [0, 1, 2]


if __name__ == '__main__':
    main()
