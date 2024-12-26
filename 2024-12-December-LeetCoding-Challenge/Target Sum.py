from functools import lru_cache
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dfs(idx: int = 0, curr_sum: int = 0) -> int:
            if idx == len(nums):
                return curr_sum == target
            return dfs(idx+1, curr_sum+nums[idx]) + dfs(idx+1, curr_sum-nums[idx])
        return dfs()


def main():
    nums = [1, 1, 1, 1, 1]
    target = 3
    assert Solution().findTargetSumWays(nums, target) == 5

    nums = [1]
    target = 1
    assert Solution().findTargetSumWays(nums, target) == 1


if __name__ == '__main__':
    main()
