# -*- coding: utf-8 -*-
from typing import List


class NaiveSolution:
    '''
    Brute force solution. Leads to TLE.
    Time Complexity: O(n^4)
    '''
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = list()
        if n < 4:
            return ans
        for i in range(0, n-3):
            for j in range(i+1, n-2):
                for k in range(j+1, n-1):
                    for l in range(k+1, n):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            temp = sorted([nums[i], nums[j], nums[k], nums[l]])
                            if temp not in ans:
                                ans.append(temp)
        return ans


class Solution:
    '''
    Solution is based on extending the 3Sum problem. Pairs are grouped
    according to their sum. For every sum, check if target - sum exists.
    Compare indices to ensure distinct elements.
    Time Complexity: O(n^2)
    '''
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = list()
        # Base condition
        if n < 4:
            return ans

        # Hashmap of sums of pairs to a tuple of pair indices
        pair_sums = dict()
        for i in range(0, n-1):
            for j in range(i+1, n):
                s = nums[i] + nums[j]
                if s in pair_sums:
                    pair_sums[s].append((i, j))
                else:
                    pair_sums[s] = [(i, j)]

        for s, pairs1 in pair_sums.items():  # All tuples of pairs with sums s
            req = target - s
            if req in pair_sums:
                pairs2 = pair_sums[req]  # All tuples of pairs for target - s

                for i, j in pairs1:  # Indices from pairs1
                    for k, l in pairs2:  # Indices from pairs2
                        # Check if distinct indices
                        if len(set([i, j, k, l])) == 4:
                            temp = sorted([nums[i], nums[j], nums[k], nums[l]])
                            # 4 sums in answer must be distinct
                            if temp not in ans:
                                ans.append(temp)

        return ans


def main():
    obj = Solution()

    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    assert sorted(obj.fourSum(nums, target)) == sorted([[-2, -1, 1, 2],
                                                        [-2, 0, 0, 2],
                                                        [-1, 0, 0, 1]])

    nums = [2, 2, 2, 2, 2]
    target = 8
    assert obj.fourSum(nums, target) == [[2, 2, 2, 2]]


if __name__ == '__main__':
    main()
