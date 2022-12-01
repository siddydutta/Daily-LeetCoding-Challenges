# -*- coding: utf-8 -*-
VOWELS = {'a', 'e', 'i', 'o', 'u'}


class Solution:
    def __count_vowels(self, string: str) -> int:
        count = int()
        for ch in string.lower():
            count += ch in VOWELS
        return count

    def halvesAreAlike(self, s: str) -> bool:
        half = len(s) // 2
        count1 = self.__count_vowels(s[:half])
        count2 = self.__count_vowels(s[half:])
        return count1 == count2


def main():
    s = "book"
    assert Solution().halvesAreAlike(s)

    s = "textbook"
    assert not Solution().halvesAreAlike(s)


if __name__ == '__main__':
    main()
