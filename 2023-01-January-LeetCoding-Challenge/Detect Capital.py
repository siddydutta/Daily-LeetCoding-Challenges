# -*- coding: utf-8 -*-
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()


def main():
    word = "USA"
    assert Solution().detectCapitalUse(word)

    word = "FlaG"
    assert not Solution().detectCapitalUse(word)


if __name__ == '__main__':
    main()
