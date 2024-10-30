from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        dpf = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    dpf[i] = max(dpf[i], 1+dpf[j])
        dpb = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i-1, -1, -1):
                if nums[i] > nums[j]:
                    dpb[i] = max(dpb[i], 1+dpb[j])
        max_len = 0
        for i in range(1, len(nums)-1):
            if dpf[i] > 1 and dpb[i] > 1:
                max_len = max(max_len, dpf[i]+dpb[i]-1)
        return len(nums) - max_len


def main():
    nums = [1, 3, 1]
    assert Solution().minimumMountainRemovals(nums) == 0

    nums = [2, 1, 1, 5, 6, 2, 3, 1]
    assert Solution().minimumMountainRemovals(nums) == 3


if __name__ == '__main__':
    main()
