# -*- coding: utf-8 -*-
from collections import Counter
from math import inf


class Solution:
    '''
    Solution based on two pointers and hashmap.
    Time Complexity: O(len(s) + len(t))
    '''
    def minWindow(self, s: str, t: str) -> str:
        counter = len(t)  # Number of characters needed
        ch_counts = Counter(t)  # Hashmap of character counts

        left = 0
        right = 0  # Right pointer is non-inclusive

        min_string = ""
        min_string_length = inf

        while right < len(s):
            # Take next character from s
            if s[right] in ch_counts:
                # If next character is required
                if ch_counts[s[right]] > 0:
                    counter -= 1  # Included in substring
                ch_counts[s[right]] -= 1
            right += 1

            while counter == 0:
                # Substring is valid
                string_length = right - left
                if string_length < min_string_length:
                    # Found a smaller valid substring
                    min_string = s[left:right]
                    min_string_length = string_length
                # Remove characters from start as long as valid
                if s[left] in ch_counts:
                    ch_counts[s[left]] += 1
                    if ch_counts[s[left]] > 0:
                        counter += 1  # Required in substring
                left += 1

        return min_string


def main():
    s = "ADOBECODEBANC"
    t = "ABC"
    assert Solution().minWindow(s, t) == "BANC"

    s = "a"
    t = "a"
    assert Solution().minWindow(s, t) == "a"

    s = "a"
    t = "aa"
    assert Solution().minWindow(s, t) == ""

    s = "bba"
    t = "ab"
    assert Solution().minWindow(s, t) == "ba"


if __name__ == '__main__':
    main()
