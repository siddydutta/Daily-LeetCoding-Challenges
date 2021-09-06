# -*- coding: utf-8 -*-
from typing import List
from collections import defaultdict
from bisect import bisect_left


class Solution1:
    '''
    Naive brute force solution, leads to TLE.
    '''
    def __isSubSequence(self, string1, string2, m, n):
        # Base Cases
        if m == 0:
            return True
        if n == 0:
            return False

        # If last characters of two strings are matching
        if string1[m-1] == string2[n-1]:
            return self.__isSubSequence(string1, string2, m-1, n-1)
        # If last characters are not matching
        return self.__isSubSequence(string1, string2, m, n-1)

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        n = len(s)
        for word in words:
            if self.__isSubSequence(word, s, len(word), n):
                ans += 1
        return ans


class Solution2:
    '''
    Another naive brute force solution, eliminating the need to check
    duplicate words. As observed by test case leading to TLE.
    '''
    def __isSubSequence(self, string1, string2, m, n):
        # Base Cases
        if m == 0:
            return True
        if n == 0:
            return False

        # If last characters of two strings are matching
        if string1[m-1] == string2[n-1]:
            return self.__isSubSequence(string1, string2, m-1, n-1)
        # If last characters are not matching
        return self.__isSubSequence(string1, string2, m, n-1)

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        n = len(s)
        word_count = {word: words.count(word) for word in set(words)}
        for word, count in word_count.items():
            if self.__isSubSequence(word, s, len(word), n):
                ans += count
        return ans


class Solution3:
    '''
    Optimizes the isSubSequence method to check using binary search principles.
    Time Complexity: O(m*log n + n)
    '''
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # To remove re-checking of duplicate words
        word_count = {word: words.count(word) for word in set(words)}
        # Creating a dictionary of characters and their indices in s
        indices = defaultdict(list)  # defaultdict takes care of missing keys
        for index, ch in enumerate(s):
            indices[ch].append(index)

        def isSubSequence(word):
            ptr = 0
            for ch in word:
                # Find the index of character in word
                index = bisect_left(indices[ch], ptr)
                if index >= len(indices[ch]):
                    return False  # Not a subsequence
                ptr = indices[ch][index] + 1  # Move pointer to next index
            return True

        ans = 0
        for word, count in word_count.items():
            if isSubSequence(word):
                ans += count
        return ans


class Solution:
    '''
    Simple Pythonic solution, most optimal.
    '''
    def __isSubsequence(self, word, s):
        index = 0
        for ch in word:
            # Try to find character in substring after index
            index = s.find(ch, index) + 1
            if not index:
                return False  # Not found, hence not subsequence
        return True

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        word_count = {word: words.count(word) for word in set(words)}
        ans = 0
        for word, count in word_count.items():
            if self.__isSubsequence(word, s):
                ans += count
        return ans


def main():
    obj = Solution()
    s = "abcde"
    words = ["a", "bb", "acd", "ace"]
    assert obj.numMatchingSubseq(s, words) == 3

    s = "dsahjpjauf"
    words = ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]
    assert obj.numMatchingSubseq(s, words) == 2


if __name__ == '__main__':
    main()
