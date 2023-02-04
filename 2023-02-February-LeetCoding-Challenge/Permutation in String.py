# -*- coding: utf-8 -*-
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size = len(s1)  # Length of sliding window
        s1_freq = Counter(s1)
        for i in range(len(s2)-size+1):
            string = s2[i:i+size]
            string_freq = Counter(string)
            if s1_freq == string_freq:
                return True
        return False


def main():
    s1 = "ab"
    s2 = "eidbaooo"
    assert Solution().checkInclusion(s1, s2)

    s1 = "ab"
    s2 = "eidboaoo"
    assert not Solution().checkInclusion(s1, s2)


if __name__ == '__main__':
    main()
