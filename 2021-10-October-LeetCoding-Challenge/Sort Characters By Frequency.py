# -*- coding: utf-8 -*-
from collections import Counter


class Solution:
    ''' Simple Pythonic solution. '''
    def frequencySort(self, s: str) -> str:
        return "".join([ch*freq for ch, freq in Counter(s).most_common()])


def main():
    s = "tree"
    assert Solution().frequencySort(s) in ("eert", "eetr")

    s = "cccaaa"
    assert Solution().frequencySort(s) in ("aaaccc", "cccaaa")

    s = "Aabb"
    assert Solution().frequencySort(s) in ("bbAa", "bbaA")


if __name__ == '__main__':
    main()
