VOWELS = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}


class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = sorted([ch for ch in s if ch in VOWELS])
        s = list(s)
        for i, ch in enumerate(s):
            if ch in VOWELS:
                s[i] = vowels.pop(0)
        return ''.join(s)


def main():
    s = 'lEetcOde'
    assert Solution().sortVowels(s) == 'lEOtcede'

    s = 'lYmpH'
    assert Solution().sortVowels(s) == 'lYmpH'


if __name__ == '__main__':
    main()
