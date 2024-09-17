from collections import Counter
from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words_freq = Counter(f'{s1} {s2}'.split())
        return [word for word, freq in words_freq.items() if freq == 1]


def main():
    s1 = 'this apple is sweet'
    s2 = 'this apple is sour'
    assert Solution().uncommonFromSentences(s1, s2) == ['sweet', 'sour']

    s1 = 'apple apple'
    s2 = 'banana'
    assert Solution().uncommonFromSentences(s1, s2) == ['banana']


if __name__ == '__main__':
    main()
