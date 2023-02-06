# -*- coding: utf-8 -*-
from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        size = len(p)  # Sliding window size
        p_map = Counter(p)  # {ch: count(ch) for ch in p}
        s_map = Counter(s[:size])  # map of first window

        indices = [0] if p_map == s_map else []
        for i in range(1, len(s)-size+1):
            s_map[s[i-1]] -= 1  # Remove first character of window
            s_map[s[i+size-1]] += 1  # Add next character
            if s_map == p_map:
                indices.append(i)
        return indices


def main():
    s = "cbaebabacd"
    p = "abc"
    # TODO Check this test case
    # assert Solution().findAnagrams(s, p) == [6, 0]

    s = "abab"
    p = "ab"
    assert Solution().findAnagrams(s, p) == [0, 1, 2]


if __name__ == '__main__':
    main()
