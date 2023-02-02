# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def __init__(self):
        self.ch_map = None

    def compare(self, word1, word2):
        '''
        Returns 1 if word1 < word2
                -1 if word1 > word2
                0 if word1 == word2
        '''
        if word1 == word2:
            return 0

        ptr1, ptr2 = 0, 0
        while ptr1 < len(word1) and ptr2 < len(word2):
            if self.ch_map[word1[ptr1]] > self.ch_map[word2[ptr2]]:
                return -1
            elif self.ch_map[word1[ptr1]] < self.ch_map[word2[ptr2]]:
                return 1
            else:
                ptr1 += 1
                ptr2 += 1

        return 1 if ptr1 == len(word1) else -1

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        self.ch_map = {order[ch]: ch for ch in range(len(order))}
        for i in range(len(words)-1):
            if self.compare(words[i], words[i+1]) < 0:
                return False
        return True


def main():
    words = ["hello", "leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    assert Solution().isAlienSorted(words, order)

    words = ["word", "world", "row"]
    order = "worldabcefghijkmnpqstuvxyz"
    assert not Solution().isAlienSorted(words, order)

    words = ["apple", "app"]
    order = "abcdefghijklmnopqrstuvwxyz"
    assert not Solution().isAlienSorted(words, order)


if __name__ == '__main__':
    main()
