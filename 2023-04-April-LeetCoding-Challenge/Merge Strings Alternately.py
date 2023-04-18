# -*- coding: utf-8 -*-
from itertools import zip_longest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join(ch1+ch2 for ch1, ch2 in zip_longest(word1, word2, fillvalue=''))


def main():
    word1, word2 = "abc", "pqr"
    assert Solution().mergeAlternately(word1, word2) == "apbqcr"

    word1, word2 = "ab", "pqrs"
    assert Solution().mergeAlternately(word1, word2) == "apbqrs"

    word1, word2 = "abcd", "pq"
    assert Solution().mergeAlternately(word1, word2) == "apbqcd"


if __name__ == '__main__':
    main()
