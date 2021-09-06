# -*- coding: utf-8 -*-
from itertools import combinations
from typing import List


class IterativeSolution:
    ''' Simple Python solution using sort, set and combinations. '''
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = list()
        nums.sort()  # To skip over duplicate combinations
        for length in range(len(nums)+1):
            combo = set(combinations(nums, length))  # Get sets of length
            subsets += list(map(list, combo))  # Add all distinct to result
        return subsets


class RecursiveSolution:
    ''' Backtracking solution. '''
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        def backtrack(subset: List[int], start: int, length: int) -> None:
            # Base condition
            if len(subset) == length:
                subsets.append(subset.copy())
                return
            for i in range(start, n):
                if i > start and nums[i] == nums[i-1]:
                    # Prevent duplicate subsets
                    continue
                subset.append(nums[i])  # Append next character
                backtrack(subset, i+1, length)  # Recursive with next start pos
                subset.pop()  # Remove last character to backtrack
            return

        subsets = list()
        for length in range(0, n+1):
            backtrack(list(), 0, length)  # Add all subsets of length
        return subsets


def main():
    solutions = [IterativeSolution(), RecursiveSolution()]
    for obj in solutions:
        nums = [1, 2, 2]
        exp_ans = sorted([[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])
        ans = sorted(obj.subsetsWithDup(nums))
        assert exp_ans == ans


if __name__ == '__main__':
    main()
