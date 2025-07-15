class Solution:
    VOWELS = {'a', 'e', 'i', 'o', 'u'}

    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        has_vowel, has_consonant = False, False
        for ch in word.lower():
            if not ch.isalpha():
                if not ch.isdigit():
                    return False
            else:
                if ch in self.VOWELS:
                    has_vowel = True
                else:
                    has_consonant = True
        return has_vowel and has_consonant


def main():
    word = '234Adas'
    assert Solution().isValid(word) is True

    word = 'b3'
    assert Solution().isValid(word) is False

    word = 'a3$e'
    assert Solution().isValid(word) is False


if __name__ == '__main__':
    main()
