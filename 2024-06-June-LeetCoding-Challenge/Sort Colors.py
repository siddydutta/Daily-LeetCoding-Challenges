from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums)-1
        ptr = 0

        while ptr <= right:
            if nums[ptr] == 0:
                # swap 0 to beginning
                nums[ptr], nums[left] = nums[left], nums[ptr]
                left += 1
                ptr += 1
            elif nums[ptr] == 1:
                # keep 1 in the middle
                ptr += 1
            elif nums[ptr] == 2:
                # swap 2 to the end
                nums[ptr], nums[right] = nums[right], nums[ptr]
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
