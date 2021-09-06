# -*- coding: utf-8 -*-
from typing import List, Set


class NaiveSolution:
    '''
    Brute force solution. Building set s using DFS.
    Time Complexity: O(n^2)
    '''
    def arrayNesting(self, nums: List[int]) -> int:

        def dfs(index: int, elements: Set[int]) -> None:
            ''' Keep traversing until a cycle is formed. '''
            if nums[index] in elements:
                s.append(elements)
                return  # Cycle condition
            elements.add(nums[index])
            dfs(nums[index], elements)  # Try next index

        s = list()
        for k in range(len(nums)):
            dfs(k, set())

        return len(max(s, key=lambda s_k: len(s_k)))


class Solution:
    '''
    Avoid recomputations by flagging indices already visited.
    If an index is already included in the cycle, no need to try it again.
    Time Complexity: O(n)
    '''
    def arrayNesting(self, nums: List[int]) -> int:
        visited = [0] * len(nums)
        max_length = 0

        for i in nums:
            length = 0
            # Traverse and mark until cycle is formed, if unvisited
            while not visited[i]:
                visited[i] = 1  # Mark as visited
                length += 1     # Increment length
                i = nums[i]     # Next index
            max_length = max(max_length, length)

        return max_length


def main():
    nums = [5, 4, 0, 3, 1, 6, 2]
    assert Solution().arrayNesting(nums) == 4

    nums = [0, 1, 2]
    assert Solution().arrayNesting(nums) == 1


if __name__ == '__main__':
    main()
