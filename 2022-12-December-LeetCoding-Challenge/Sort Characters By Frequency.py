# -*- coding: utf-8 -*-
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join([ch * freq for ch, freq in Counter(s).most_common()])


def main():
    s = "tree"
    assert Solution().frequencySort(s) == "eetr"

    s = "cccaaa"
    assert Solution().frequencySort(s) == "cccaaa"

    s = "Aabb"
    assert Solution().frequencySort(s) == "bbAa"


if __name__ == '__main__':
    main()
