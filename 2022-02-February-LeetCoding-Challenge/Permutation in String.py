# -*- coding: utf-8 -*-
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ''' Sliding window and hashmap based solution. '''
        size = len(s1)  # Length of sliding window
        s1_freq = Counter(s1)  # Required frequencies
        for i in range(len(s2)-size+1):
            # Get all substrings of s1 size from s2
            string_freq = Counter(s2[i:i+size])
            # Check if frequencies of characters are equal
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
