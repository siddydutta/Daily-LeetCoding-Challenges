from collections import Counter
from functools import reduce
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        counts = [Counter(word) for word in words]
        common_counts = reduce(lambda x, y: x & y, counts)
        result = []
        for char, count in common_counts.items():
            result.extend([char] * count)
        return result


def main():
    words = ['bella', 'label', 'roller']
    assert Solution().commonChars(words) == ['e', 'l', 'l']

    words = ['cool', 'lock', 'cook']
    assert Solution().commonChars(words) == ['c', 'o']


if __name__ == '__main__':
    main()
