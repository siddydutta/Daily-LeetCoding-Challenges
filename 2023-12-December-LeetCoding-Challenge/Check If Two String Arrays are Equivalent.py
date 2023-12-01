from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)


def main():
    word1 = ["ab", "c"]
    word2 = ["a", "bc"]
    assert Solution().arrayStringsAreEqual(word1, word2)

    word1 = ["a", "cb"]
    word2 = ["ab", "c"]
    assert not Solution().arrayStringsAreEqual(word1, word2)

    word1 = ["abc", "d", "defg"]
    word2 = ["abcddefg"]
    assert Solution().arrayStringsAreEqual(word1, word2)


if __name__ == '__main__':
    main()
