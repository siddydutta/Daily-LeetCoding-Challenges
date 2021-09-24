# -*- coding: utf-8 -*-
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""  # Not possible to break

        # Track only half of string as it is a palindrome
        for i in range(len(palindrome) // 2):
            if palindrome[i] != 'a':
                # Change first non 'a' character to 'a'
                return palindrome[:i] + 'a' + palindrome[i+1:]

        # If string has only 'a', change last character to 'b'
        return palindrome[:-1] + 'b'


def main():
    palindrome = "abccba"
    assert Solution().breakPalindrome(palindrome) == "aaccba"

    palindrome = "a"
    assert Solution().breakPalindrome(palindrome) == ""

    palindrome = "aa"
    assert Solution().breakPalindrome(palindrome) == "ab"

    palindrome = "aba"
    assert Solution().breakPalindrome(palindrome) == "abb"


if __name__ == '__main__':
    main()
