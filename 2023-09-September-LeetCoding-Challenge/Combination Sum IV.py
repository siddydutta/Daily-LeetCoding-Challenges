from functools import lru_cache
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        @lru_cache(None)
        def dfs(rem: int) -> int:
            if rem < 0:
                return 0
            elif rem == 0:
                return 1
            count = 0
            for num in nums:
                count += dfs(rem - num)
            return count

        return dfs(target)


def main():
    nums = [1, 2, 3]
    target = 4
    assert Solution().combinationSum4(nums, target) == 7

    nums = [9]
    target = 3
    assert Solution().combinationSum4(nums, target) == 0


if __name__ == '__main__':
    main()
