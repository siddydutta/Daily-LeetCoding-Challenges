# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ''' Backtracking based solution using DFS. '''
        partitions = list()

        def dfs(substring: str, path: List[str]) -> None:
            if not substring:
                partitions.append(path.copy())
                return  # Base condition
            for i in range(1, len(substring)+1):
                if substring[:i] == substring[:i][::-1]:
                    # If palindrome
                    path.append(substring[:i])
                    dfs(substring[i:], path)  # Check substrings
                    path.pop()  # Pop to backtrack

        dfs(s, list())
        return partitions


def main():
    s = "aab"
    assert Solution().partition(s) == [["a", "a", "b"], ["aa", "b"]]

    s = "a"
    assert Solution().partition(s) == [["a"]]


if __name__ == '__main__':
    main()
