from typing import List


class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        # build monotonic decreasing stack of indices
        for i in range(len(nums)):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        # find maximum width ramp
        max_width = 0
        for j in range(len(nums)-1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                max_width = max(max_width, j-stack.pop())
        return max_width


def main():
    nums = [6, 0, 8, 2, 1, 5]
    assert Solution().maxWidthRamp(nums) == 4

    nums = [9, 8, 1, 0, 1, 9, 4, 0, 4, 1]
    assert Solution().maxWidthRamp(nums) == 7


if __name__ == '__main__':
    main()
