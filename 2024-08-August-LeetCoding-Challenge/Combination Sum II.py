from copy import deepcopy
from typing import List


class Solution:
    def combinationSum2(
            self, candidates: List[int], target: int
    ) -> List[List[int]]:

        def combine(idx: int, combo: List[int], curr_sum: int) -> None:
            if curr_sum == target:
                nonlocal combos
                # since lists are used by reference
                combos.append(deepcopy(combo))
                return
            elif curr_sum > target:
                return

            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue  # skip duplicates
                combo.append(candidates[i])
                combine(i+1, combo, curr_sum+candidates[i])
                combo.pop()  # backtrack

        candidates.sort()  # to help handle duplicates
        combos = list()
        combine(0, [], 0)
        return combos


def main():
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    assert Solution().combinationSum2(candidates, target) == [[1, 1, 6],
                                                              [1, 2, 5],
                                                              [1, 7],
                                                              [2, 6]]

    candidates = [2, 5, 2, 1, 2]
    target = 5
    assert Solution().combinationSum2(candidates, target) == [[1, 2, 2],
                                                              [5]]


if __name__ == '__main__':
    main()
