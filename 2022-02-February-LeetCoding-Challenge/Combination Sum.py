# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:
        ''' Backtracking using DFS based solution. '''
        def dfs(nums: List[int], target: int, path: List[int]) -> None:
            if target < 0:
                return
            if target == 0:
                # Path numbers equal target
                combinations.append(path)
                return
            for i in range(len(nums)):
                # DFS with remaining numbers, subtract target and add to path
                dfs(nums[i:], target-nums[i], path+[nums[i]])

        combinations = list()
        dfs(candidates, target, list())
        return combinations


def main():
    candidates = [2, 3, 6, 7]
    target = 7
    assert Solution().combinationSum(candidates, target) == [[2, 2, 3], [7]]

    candidates = [2, 3, 5]
    target = 8
    assert Solution().combinationSum(candidates, target) == [[2, 2, 2, 2],
                                                             [2, 3, 3], [3, 5]]

    candidates = [2]
    target = 1
    assert Solution().combinationSum(candidates, target) == []


if __name__ == '__main__':
    main()
