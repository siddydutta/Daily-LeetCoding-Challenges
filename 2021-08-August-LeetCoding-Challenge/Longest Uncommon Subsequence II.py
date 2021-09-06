# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def is_subsequence(self, word1, word2):
        ''' Checks if word1 is a subsequence of word2. '''
        n = len(word1)
        index = 0  # Pointer for word1
        for ch in word2:
            if index < n and ch == word1[index]:
                index += 1
        return index == n  # All characters in word1 accounted for

    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(key=len, reverse=True)  # Sort by decreasing order of length
        for s in strs:
            # Is s a subsequence of all other strs
            res = [self.is_subsequence(s, t) for t in strs]
            if sum(res) == 1:
                return len(s)  # Will be max, as strings are reverse sorted
        return -1


def main():
    strs = ["aba", "cdc", "eae"]
    assert Solution().findLUSlength(strs) == 3

    strs = ["aaa", "aaa", "aa"]
    assert Solution().findLUSlength(strs) == -1


if __name__ == '__main__':
    main()
