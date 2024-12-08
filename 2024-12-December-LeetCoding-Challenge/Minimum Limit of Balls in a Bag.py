from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        ptr1, ptr2 = 1, max(nums)
        while ptr1 < ptr2:
            mid = (ptr1 + ptr2) // 2
            if sum((n - 1) // mid for n in nums) <= maxOperations:
                ptr2 = mid
            else:
                ptr1 = mid + 1
        return ptr2


def main():
    nums = [9]
    maxOperations = 2
    assert Solution().minimumSize(nums, maxOperations) == 3

    nums = [2, 4, 8, 2]
    maxOperations = 4
    assert Solution().minimumSize(nums, maxOperations) == 2


if __name__ == '__main__':
    main()
