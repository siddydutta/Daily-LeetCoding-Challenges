# -*- coding: utf-8 -*-
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        ''' Simple Pythonic solution. '''
        return word.isupper() or word.islower() or word.istitle()


def main():
    word = "USA"
    assert Solution().detectCapitalUse(word)

    word = "leetcode"
    assert Solution().detectCapitalUse(word)

    word = "Google"
    assert Solution().detectCapitalUse(word)

    word = "FlaG"
    assert not Solution().detectCapitalUse(word)


if __name__ == '__main__':
    main()
