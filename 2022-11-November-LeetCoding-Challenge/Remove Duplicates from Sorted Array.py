from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1 if len(nums) > 0 else 0
        for n in nums:
            if n != nums[index-1]:
                nums[index] = n
                index += 1
        return index


def main():
    nums = [1, 1, 2]
    assert Solution().removeDuplicates(nums) == 2

    nums = nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    assert Solution().removeDuplicates(nums) == 5


if __name__ == '__main__':
    main()
