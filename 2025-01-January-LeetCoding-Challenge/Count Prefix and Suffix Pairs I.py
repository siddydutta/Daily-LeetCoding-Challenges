from itertools import combinations
from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for str1, str2 in combinations(words, 2):
            count += str2.startswith(str1) and str2.endswith(str1)
        return count


def main():
    words = ['a', 'aba', 'ababa', 'aa']
    assert Solution().countPrefixSuffixPairs(words) == 4

    words = ['pa', 'papa', 'ma', 'mama']
    assert Solution().countPrefixSuffixPairs(words) == 2

    words = ['abab', 'ab']
    assert Solution().countPrefixSuffixPairs(words) == 0


if __name__ == '__main__':
    main()
