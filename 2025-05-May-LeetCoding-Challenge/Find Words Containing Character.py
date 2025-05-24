class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        return [i for i, word in enumerate(words) if x in word]


def main():
    words = ['leet', 'code']
    x = 'e'
    assert Solution().findWordsContaining(words, x) == [0, 1]

    words = ['abc', 'bcd', 'aaaa', 'cbc']
    x = 'a'
    assert Solution().findWordsContaining(words, x) == [0, 2]

    words = ['abc', 'bcd', 'aaaa', 'cbc']
    x = 'z'
    assert Solution().findWordsContaining(words, x) == []


if __name__ == '__main__':
    main()
