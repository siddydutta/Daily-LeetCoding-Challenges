from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1, freq2 = Counter(word1), Counter(word2)
        return freq1.keys() == freq2.keys() and sorted(freq1.values()) == sorted(freq2.values())


def main():
    word1 = 'abc'
    word2 = 'bca'
    assert Solution().closeStrings(word1, word2) is True

    word1 = 'a'
    word2 = 'aa'
    assert Solution().closeStrings(word1, word2) is False

    word1 = 'cabbba'
    word2 = 'abbccc'
    assert Solution().closeStrings(word1, word2) is True


if __name__ == '__main__':
    main()
