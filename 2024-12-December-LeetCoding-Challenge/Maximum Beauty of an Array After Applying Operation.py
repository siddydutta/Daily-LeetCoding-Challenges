from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        ptr1 = 0
        for ptr2 in range(len(nums)):
            if nums[ptr2]-nums[ptr1] > k*2:
                ptr1 += 1
        return ptr2-ptr1+1


def main():
    nums = [4, 6, 1, 2]
    k = 2
    assert Solution().maximumBeauty(nums, k) == 3

    nums = [1, 1, 1, 1]
    k = 10
    assert Solution().maximumBeauty(nums, k) == 4


if __name__ == '__main__':
    main()
