# -*- coding: utf-8 -*-
from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        return str1[:gcd(len(str1), len(str2))]


def main():
    str1 = "ABCABC"
    str2 = "ABC"
    assert Solution().gcdOfStrings(str1, str2) == "ABC"

    str1 = "ABABAB"
    str2 = "ABAB"
    assert Solution().gcdOfStrings(str1, str2) == "AB"

    str1 = "LEET"
    str2 = "CODE"
    assert Solution().gcdOfStrings(str1, str2) == ""


if __name__ == '__main__':
    main()
