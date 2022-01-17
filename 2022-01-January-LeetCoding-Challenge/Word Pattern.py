# -*- coding: utf-8 -*-
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ''' Simple solution using hashmap and set. '''
        table, seen_words = dict(), set()
        words = s.split()
        if len(pattern) != len(words):
            return False
        for ch, word in zip(pattern, words):
            if ch not in table:
                if word not in seen_words:
                    table[ch] = word
                    seen_words.add(word)
                else:
                    return False  # ch should be in map
            else:
                if table[ch] != word:
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
