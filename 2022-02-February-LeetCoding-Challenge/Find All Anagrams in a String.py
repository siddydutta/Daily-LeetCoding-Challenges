# -*- coding: utf-8 -*-
from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ''' Hashmap and sliding window based solution. '''
        size = len(p)  # Sliding window size
        p_map = Counter(p)  # {ch: count(ch) for ch in p}
        s_map = Counter(s[:size])  # map of first window

        indices = [0] if p_map == s_map else []
        for i in range(1, len(s)-size+1):
            s_map[s[i-1]] -= 1  # Remove first character of window
            s_map[s[i+size-1]] += 1  # Add next character
            # if s_map == p_map:
            if all(s_map[k] == p_map[k] for k in set(s_map) | set(p_map)):
                indices.append(i)
        return indices


def main():
    s = "cbaebabacd"
    p = "abc"
    assert Solution().findAnagrams(s, p) == [0, 6]

    s = "abab"
    p = "ab"
    assert Solution().findAnagrams(s, p) == [0, 1, 2]


if __name__ == '__main__':
    main()
