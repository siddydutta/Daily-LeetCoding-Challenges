# -*- coding: utf-8 -*-
from functools import lru_cache


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(None)
        def check_palindrome(left: int, right: int) -> int:
            if left == right:
                return 1
            elif left > right:
                return 0
            elif s[left] == s[right]:
                return 2 + check_palindrome(left+1, right-1)
            else:
                return max(check_palindrome(left+1, right),
                           check_palindrome(left, right-1))
        return check_palindrome(0, len(s)-1)


def main():
    s = "bbbab"
    assert Solution().longestPalindromeSubseq(s) == 4

    s = "cbbd"
    assert Solution().longestPalindromeSubseq(s) == 2


if __name__ == '__main__':
    main()
