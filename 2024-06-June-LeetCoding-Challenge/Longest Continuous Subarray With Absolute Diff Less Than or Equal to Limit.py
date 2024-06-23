from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # store index of max and min digits in current window
        max_d, min_d = deque(), deque()
        left = 0
        result = 0
        for right in range(len(nums)):
            # extend window on the right
            # maintain max and min digits in current window
            while max_d and nums[max_d[-1]] <= nums[right]:
                max_d.pop()
            max_d.append(right)
            while min_d and nums[min_d[-1]] >= nums[right]:
                min_d.pop()
            min_d.append(right)

            while nums[max_d[0]] - nums[min_d[0]] > limit:
                # if diff > limit, shrink window from left
                left += 1
                # remove digit if exists
                if max_d[0] < left:
                    max_d.popleft()
                if min_d[0] < left:
                    min_d.popleft()

            # update result
            result = max(result, right-left+1)
        return result


def main():
    nums = [8, 2, 4, 7]
    limit = 4
    assert Solution().longestSubarray(nums, limit) == 2

    nums = [10, 1, 2, 4, 7, 2]
    limit = 5
    assert Solution().longestSubarray(nums, limit) == 4


if __name__ == '__main__':
    main()
