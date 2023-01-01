# -*- coding: utf-8 -*-
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        table = dict()
        words = s.split()

        if len(pattern) != len(words):
            return False
        if len(set(pattern)) != len(set(words)):
            return False

        for ch, word in zip(pattern, words):
            if word not in table:
                table[word] = ch
            elif table.get(word) != ch:
                return False
        return True


def main():
    pattern = "abba"
    s = "dog cat cat dog"
    assert Solution().wordPattern(pattern, s)

    pattern = "abba"
    s = "dog cat cat fish"
    assert not Solution().wordPattern(pattern, s)

    pattern = "aaaa"
    s = "dog cat cat dog"
    assert not Solution().wordPattern(pattern, s)


if __name__ == '__main__':
    main()
