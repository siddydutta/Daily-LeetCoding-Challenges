from collections import Counter
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq = Counter(words)
        length, centered = 0, False

        for word, count in freq.items():
            # if word itself is a palindrome
            if word[0] == word[1]:
                if count % 2 == 0:
                    length += count
                else:
                    # one of the occurrences is centered
                    length += count-1
                    centered = True
            # avoid repeated palindrome
            elif word[0] < word[1]:
                length += 2 * min(count, freq[word[::-1]])

        if centered:
            length += 1
        return 2 * length


def main():
    words = ["lc", "cl", "gg"]
    assert Solution().longestPalindrome(words) == 6

    words = ["ab", "ty", "yt", "lc", "cl", "ab"]
    assert Solution().longestPalindrome(words) == 8

    words = ["cc", "ll", "xx"]
    assert Solution().longestPalindrome(words) == 2


if __name__ == '__main__':
    main()
