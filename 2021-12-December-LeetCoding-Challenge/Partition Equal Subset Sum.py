# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        ''' Recursive DFS with memoization based solution. '''
        total = sum(nums)
        # Can only partition if total sum is even
        if total % 2 != 0:
            return False
        else:
            total = total // 2  # Target sum

        def dfs(index: int, target: int) -> bool:
            ''' Returns if current choice of numbers has reached target. '''
            if target < 0 or target in cache:
                return False  # Already computed
            if target == 0:
                return True

            cache.add(target)
            # for i in range(index, n):
            #     if dfs(i+1, target-nums[i]):
            for i, num in enumerate(nums[index:], index):
                if dfs(i+1, target-num):
                    return True
            return False

        cache = set()
        return dfs(0, total)


def main():
    nums = [1, 5, 11, 5]
    assert Solution().canPartition(nums)

    nums = [1, 2, 3, 5]
    assert not Solution().canPartition(nums)


if __name__ == '__main__':
    main()
