# -*- coding: utf-8 -*-
from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1, freq2 = Counter(word1), Counter(word2)
        return freq1.keys() == freq2.keys() and \
            sorted(freq1.values()) == sorted(freq2.values())


def main():
    word1, word2 = "abc", "bca"
    assert Solution().closeStrings(word1, word2)

    word1, word2 = "a", "aa"
    assert not Solution().closeStrings(word1, word2)

    word1, word2 = "cabbba", "abbccc"
    assert Solution().closeStrings(word1, word2)


if __name__ == '__main__':
    main()
